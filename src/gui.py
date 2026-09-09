import threading
import time

import customtkinter as ctk

from tkinter.scrolledtext import ScrolledText

from main import (
    select_pdf,
    summarize_pdf,
    quiz_pdf,
    flashcards_pdf,
    chat_pdf,
    chat_history,
)

from ai.quiz_parser import parse_quiz
from ai.flashcard_parser import parse_flashcards

import os
import subprocess


# =============================
# UI Colors
# =============================

NAVY = "#071A5C"
NAVY_HOVER = "#0D2A8C"

YELLOW = "#FFD21F"
YELLOW_HOVER = "#FFE45C"

WHITE = "#FFFFFF"
BLACK = "#000000"

# -----------------------------
# Theme
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AIStudyAssistantGUI(ctk.CTk):

    def __init__(self):
        super().__init__()
        # -----------------------------
        # Window Icon
        # -----------------------------
        import os
        from PIL import Image, ImageTk

        icon_path = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "assets",
                "app_icon.png",
            )
        )

        icon_image = Image.open(icon_path)
        icon_photo = ImageTk.PhotoImage(icon_image)

        self.iconphoto(False, icon_photo)

        # Keep reference to prevent garbage collection
        self._icon_photo = icon_photo



        # -----------------------------
        # Window
        # -----------------------------
        self.title("AI Study Assistant")
        self.geometry("1000x800")
        self.minsize(1000, 800)


        # -----------------------------
        # Application State
        # -----------------------------
        self.selected_pdf = None

        self.quiz_questions = []
        self.quiz_current_index = 0
        self.quiz_score = 0

        self.flashcards = []
        self.flashcard_current_index = 0
        self.flashcard_answer_visible = False
        self.is_processing = False



        # -----------------------------
        # Main Grid
        # -----------------------------
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # -----------------------------
        # Build Interface
        # -----------------------------
        self.create_header()

        self.create_status_bar()

        self.create_layout()

        self.create_buttons()

        self.create_output_box()

        self.create_quiz_frame()

        self.create_flashcard_frame()

        self.create_footer()
        self.selected_pdf = None

    def create_header(self):

        title = ctk.CTkLabel(
            self,
            text="AI Study Assistant",
            font=("Arial", 30, "bold"),
            text_color=WHITE,
        )

        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Your AI-powered PDF learning assistant",
            font=("Arial", 15),
            text_color="#A8B0C0",
        )

        subtitle.pack()

    def create_status_bar(self):

        self.status = ctk.CTkLabel(
            self,
            text="Status: Ready",
            font=("Arial", 15),
            text_color="#A8B0C0",
        )

        self.status.pack(pady=(20, 5))

        self.progress = ctk.CTkProgressBar(
            self,
            width=500,
            height=8,
        )

        self.progress.pack()

        self.progress.set(0)

    def create_layout(self):

        self.main_frame = ctk.CTkFrame(self)

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20,
        )

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=3)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.left_frame = ctk.CTkFrame(
            self.main_frame,
            corner_radius=10,
        )

        self.left_frame.grid(
            row=0,
            column=0,
            sticky="nswe",
            padx=(10, 5),
            pady=10,
        )

        self.right_frame = ctk.CTkFrame(
            self.main_frame,
            corner_radius=10,
        )

        self.right_frame.grid(
            row=0,
            column=1,
            sticky="nswe",
            padx=(5, 10),
            pady=10,
        )

        self.right_frame.grid_rowconfigure(1, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)


    def create_quiz_frame(self):

        self.quiz_frame = ctk.CTkScrollableFrame(
            self.right_frame,
            corner_radius=10,
        )

        self.quiz_title = ctk.CTkLabel(
            self.quiz_frame,
            text="Interactive Quiz",
            font=("Arial", 22, "bold"),
            text_color=WHITE,
        )

        self.quiz_title.pack(
            pady=(20, 10),
        )

        self.quiz_progress = ctk.CTkLabel(
            self.quiz_frame,
            text="Question 1",
            font=("Arial", 14),
            text_color="#A8B0C0",
        )

        self.quiz_progress.pack(
            pady=(0, 20),
        )

        self.quiz_question = ctk.CTkLabel(
            self.quiz_frame,
            text="",
            font=("Arial", 16, "bold"),
            text_color=WHITE,
            wraplength=650,
            justify="left",
        )

        self.quiz_question.pack(
            fill="x",
            padx=30,
            pady=(0, 20),
        )

        self.quiz_option_buttons = {}

        for option in ["A", "B", "C", "D"]:

            button = ctk.CTkButton(
                self.quiz_frame,
                text="",
                height=45,
                anchor="w",
                fg_color=NAVY,
                hover_color=NAVY_HOVER,
                text_color=WHITE,
                command=lambda key=option: self.answer_quiz(key),
            )

            button.pack(
                fill="x",
                padx=40,
                pady=6,
            )

            self.quiz_option_buttons[option] = button

        self.quiz_explanation = ctk.CTkLabel(
            self.quiz_frame,
            text="",
            font=("Arial", 13),
            text_color="#A8B0C0",
            wraplength=650,
            justify="left",
        )

        self.quiz_explanation.pack(
            fill="x",
            padx=40,
            pady=(20, 10),
        )

        self.quiz_next_button = ctk.CTkButton(
            self.quiz_frame,
            text="Next Question",
            height=45,
            fg_color=YELLOW,
            hover_color=YELLOW_HOVER,
            text_color=BLACK,
            command=self.next_quiz_question,
        )

        self.quiz_next_button.pack(
            pady=20,
        )


    def create_flashcard_frame(self):

        self.flashcard_frame = ctk.CTkFrame(
            self.right_frame,
            corner_radius=10,
        )

        self.flashcard_title = ctk.CTkLabel(
            self.flashcard_frame,
            text="Study Flashcards",
            font=("Arial", 22, "bold"),
            text_color=WHITE,
        )

        self.flashcard_title.pack(
            pady=(20, 10),
        )

        self.flashcard_progress = ctk.CTkLabel(
            self.flashcard_frame,
            text="Card 1 of 10",
            font=("Arial", 14),
            text_color="#A8B0C0",
        )

        self.flashcard_progress.pack(
            pady=(0, 25),
        )

        self.flashcard_question = ctk.CTkLabel(
            self.flashcard_frame,
            text="",
            font=("Arial", 17, "bold"),
            text_color=WHITE,
            wraplength=650,
            justify="left",
        )

        self.flashcard_question.pack(
            fill="x",
            padx=40,
            pady=(20, 30),
        )

        self.flashcard_answer = ctk.CTkLabel(
            self.flashcard_frame,
            text="",
            font=("Arial", 15),
            text_color="#A8B0C0",
            wraplength=650,
            justify="left",
        )

        self.flashcard_answer.pack(
            fill="x",
            padx=40,
            pady=(10, 30),
        )

        self.flashcard_show_button = ctk.CTkButton(
            self.flashcard_frame,
            text="Show Answer",
            width=220,
            height=45,
            fg_color=YELLOW,
            hover_color=YELLOW_HOVER,
            text_color=BLACK,
            font=("Arial", 14, "bold"),
            command=self.show_flashcard_answer,
        )

        self.flashcard_show_button.pack(
            pady=10,
        )

        self.flashcard_next_button = ctk.CTkButton(
            self.flashcard_frame,
            text="Next Card",
            width=220,
            height=45,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            font=("Arial", 14, "bold"),
            command=self.next_flashcard,
        )

        self.flashcard_next_button.pack(
            pady=10,
        )

    def show_quiz_settings(self):

        # Hide normal output
        self.output_box.pack_forget()

        # Hide quiz if it is already visible
        self.quiz_frame.pack_forget()

        settings_frame = ctk.CTkFrame(
            self.right_frame,
            corner_radius=10,
        )

        settings_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15,
        )

        title = ctk.CTkLabel(
            settings_frame,
            text="Quiz Settings",
            font=("Arial", 24, "bold"),
            text_color=WHITE,
        )

        title.pack(pady=(50, 30))

        questions_label = ctk.CTkLabel(
            settings_frame,
            text="Number of Questions",
            font=("Arial", 15, "bold"),
            text_color=WHITE,
        )

        questions_label.pack(pady=(10, 8))

        questions_menu = ctk.CTkOptionMenu(
            settings_frame,
            values=["5", "10", "15"],
            width=220,
            height=40,
            fg_color=NAVY,
            button_color=NAVY,
            button_hover_color=NAVY_HOVER,
        )

        questions_menu.set("5")

        questions_menu.pack(pady=(0, 25))

        difficulty_label = ctk.CTkLabel(
            settings_frame,
            text="Difficulty",
            font=("Arial", 15, "bold"),
            text_color=WHITE,
        )

        difficulty_label.pack(pady=(10, 8))

        difficulty_menu = ctk.CTkOptionMenu(
            settings_frame,
            values=["Easy", "Medium", "Hard"],
            width=220,
            height=40,
            fg_color=NAVY,
            button_color=NAVY,
            button_hover_color=NAVY_HOVER,
        )

        difficulty_menu.set("Medium")

        difficulty_menu.pack(pady=(0, 35))

        start_button = ctk.CTkButton(
            settings_frame,
            text="Start Quiz",
            width=220,
            height=45,
            fg_color=YELLOW,
            hover_color=YELLOW_HOVER,
            text_color=BLACK,
            font=("Arial", 14, "bold"),
            command=lambda: self.start_quiz(
                settings_frame,
                questions_menu.get(),
                difficulty_menu.get(),
            ),
        )

        start_button.pack(pady=15)


    def start_quiz(
        self,
        settings_frame,
        num_questions,
        difficulty,
    ):

        if settings_frame is not None:
            settings_frame.destroy()

        if not self.selected_pdf:
            self.show_output(
                "Please select a PDF first."
            )
            return

        self.start_processing(
            "Generating quiz..."
        )

        def generate_quiz():

            try:

                result = quiz_pdf(
                    self.selected_pdf,
                    num_questions=int(num_questions),
                    difficulty=difficulty.lower(),
                )

                questions = parse_quiz(
                    result
                )

                if not questions:

                    self.after(
                        0,
                        lambda: self.finish_quiz_error(
                            "Could not parse the generated quiz."
                        ),
                    )

                    return

                self.after(
                    0,
                    lambda: self.display_generated_quiz(
                        questions
                    ),
                )

            except Exception as error:

                self.after(
                    0,
                    lambda: self.finish_quiz_error(
                        f"Quiz Error:\n\n{error}"
                    ),
                )

        threading.Thread(
            target=generate_quiz,
            daemon=True,
        ).start()


    def finish_quiz_error(self, message):

        self.show_output(
            message
        )

        self.finish_processing()


    def display_generated_quiz(self, questions):

        self.quiz_questions = questions
        self.quiz_current_index = 0
        self.quiz_score = 0

        self.update_status(
            "Quiz ready",
            1.0,
        )

        # Hide normal output
        self.hide_output_area()

        # Show quiz frame
        self.quiz_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15,
        )

        self.display_quiz_question()
        self.finish_processing()


    def create_footer(self):
        footer = ctk.CTkLabel(
            self,
            text="© AI Study Assistant",
            font=("Arial", 12),
        )

        footer.pack(pady=(0, 10))


    def select_pdf_file(self):

        from tkinter import filedialog

        file_path = filedialog.askopenfilename(
            title="Select PDF",
            filetypes=[("PDF files", "*.pdf")],
        )

        if not file_path:
            return

        self.selected_pdf = file_path

        import os

        self.status.configure(
            text=f"Selected: {os.path.basename(file_path)}"
        )

    def create_buttons(self):

        button_width = 220
        button_height = 45

        # -----------------------------
        # Main Buttons
        # -----------------------------

        ctk.CTkButton(
            self.left_frame,
            text="📂 Select PDF",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.select_pdf_file,
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="📄 Summarize PDF",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.run_summary,
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="📝 Generate Quiz",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.open_quiz_settings,
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="🗂 Generate Flashcards",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.run_flashcards,
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="💬 Chat with Notes",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=lambda: threading.Thread(
                target=self.run_chat,
                daemon=True,
            ).start(),
        ).pack(pady=12, padx=15)

        # -----------------------------
        # Exit Button
        # -----------------------------

        ctk.CTkButton(
            self.left_frame,
            text="🚪 Exit",
            width=button_width,
            height=button_height,
            fg_color=YELLOW,
            hover_color=YELLOW_HOVER,
            text_color=BLACK,
            command=self.destroy,
        ).pack(pady=(30, 15), padx=15)

        # -----------------------------
        # Open Results
        # -----------------------------

        ctk.CTkButton(
            self.left_frame,
            text="📂 Open Results",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.open_results_folder,
        ).pack(pady=12, padx=15)

    def create_output_box(self):

        # -----------------------------
        # Output Title
        # -----------------------------

        self.output_title = ctk.CTkLabel(
            self.right_frame,
            text="Output",
            font=("Arial", 18, "bold"),
            text_color=WHITE,
        )

        self.output_title.pack(
            pady=(15, 10),
        )

        # -----------------------------
        # Output Box
        # -----------------------------

        self.output_box = ScrolledText(
            self.right_frame,
            wrap="word",
            font=("Consolas", 11),
            bg="#171717",
            fg="#FFFFFF",
            insertbackground="#FFFFFF",
            selectbackground=NAVY,
            selectforeground=WHITE,
            relief="flat",
            borderwidth=0,
        )

        self.output_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15),
        )

        # -----------------------------
        # Chat Frame
        # -----------------------------

        self.chat_frame = ctk.CTkFrame(
            self.right_frame,
            corner_radius=10,
        )

        self.chat_frame.pack(
            fill="x",
            padx=15,
            pady=(0, 15),
        )

        self.chat_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        # -----------------------------
        # Chat Entry
        # -----------------------------

        self.chat_entry = ctk.CTkEntry(
            self.chat_frame,
            placeholder_text="Ask something about your PDF...",
            height=40,
            fg_color="#1E1E1E",
            border_color="#3A3A3A",
            text_color=WHITE,
            placeholder_text_color="#888888",
        )

        # -----------------------------
        # Copy / Paste / Cut
        # -----------------------------

        self.chat_entry.bind(
            "<Control-c>",
            lambda event: self.chat_entry.event_generate("<<Copy>>"),
        )

        self.chat_entry.bind(
            "<Control-v>",
            lambda event: self.chat_entry.event_generate("<<Paste>>"),
        )

        self.chat_entry.bind(
            "<Control-x>",
            lambda event: self.chat_entry.event_generate("<<Cut>>"),
        )

        self.chat_entry.bind(
            "<Control-a>",
            lambda event: (
                self.chat_entry.select_range(0, "end"),
                "break",
            )[1],
        )

        # -----------------------------
        # Send with Enter
        # -----------------------------

        self.chat_entry.bind(
            "<Return>",
            lambda event: self.send_chat(),
        )

        self.chat_entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(10, 10),
            pady=10,
        )

        # -----------------------------
        # Send Button
        # -----------------------------

        self.send_button = ctk.CTkButton(
            self.chat_frame,
            text="Send",
            width=100,
            height=40,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.send_chat,
        )

        self.send_button.grid(
            row=0,
            column=1,
            padx=(0, 5),
            pady=10,
        )

        # -----------------------------
        # Clear Button
        # -----------------------------

        self.clear_button = ctk.CTkButton(
            self.chat_frame,
            text="🗑 Clear",
            width=100,
            height=40,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=self.clear_chat,
        )

        self.clear_button.grid(
            row=0,
            column=2,
            padx=(5, 10),
            pady=10,
        )

        # -----------------------------
        # Welcome Message
        # -----------------------------

        self.output_box.insert(
            "end",
            "Welcome to AI Study Assistant.\n\n"
            "Choose one of the options from the left panel.",
        )

        self.output_box.configure(
            state="disabled",
        )

    def send_chat(self):

        if not self.selected_pdf:
            self.show_output(
                "Please select a PDF first."
            )
            return

        question = self.chat_entry.get().strip()

        if not question:
            return

        # Show user message immediately
        self.output_box.configure(
            state="normal"
        )

        self.output_box.insert(
            "end",
            f"\n\nYou:\n{question}\n"
        )

        self.output_box.insert(
            "end",
            "\nAI:\nThinking...\n"
        )

        self.output_box.see("end")

        self.output_box.configure(
            state="disabled"
        )

        # Disable input while processing
        self.chat_entry.configure(
            state="disabled"
        )

        self.send_button.configure(
            state="disabled"
        )

        self.update_status(
            "Generating AI response...",
            0.5,
        )

        def generate_answer():

            try:

                answer = chat_pdf(
                    self.selected_pdf,
                    question,
                )

                self.after(
                    0,
                    lambda: self.finish_chat(
                    question,
                        answer,
                    ),
                )

            except Exception as error:

                self.after(
                    0,
                    lambda: self.finish_chat(
                        question,
                        f"Chat Error:\n\n{error}",
                    ),
                )

        threading.Thread(
            target=generate_answer,
            daemon=True,
        ).start()


    def finish_chat(self, question, answer):

        self.output_box.configure(
            state="normal"
        )

        # Remove the "Thinking..." line
        content = self.output_box.get(
            "1.0",
            "end"
        )

        thinking_text = "\nAI:\nThinking...\n"

        if thinking_text in content:
            content = content.replace(
                thinking_text,
                "",
                1
            )

            self.output_box.delete(
                "1.0",
                "end"
            )

            self.output_box.insert(
                "end",
                content
            )

        self.output_box.insert(
            "end",
            f"\nAI:\n{answer}\n"
        )

        self.output_box.see("end")

        self.output_box.configure(
            state="disabled"
        )

        self.chat_entry.configure(
            state="normal"
        )

        self.send_button.configure(
            state="normal"
        )

        self.chat_entry.delete(
            0,
            "end"
        )

        self.chat_entry.focus_set()

        self.update_status(
            "Ready",
            0
        )


    def hide_output_area(self):

        self.output_title.pack_forget()
        self.output_box.pack_forget()
        self.chat_frame.pack_forget()


    def show_output_area(self):

        self.output_title.pack(
            pady=(15, 10),
        )

        self.output_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15),
        )

        self.chat_frame.pack(
            fill="x",
            padx=15,
            pady=(0, 15),
        )

    def show_output(self, text):

        self.output_box.configure(
            state="normal",
        )

        self.output_box.delete(
            "1.0",
            "end",
        )

        self.output_box.insert(
            "end",
            text,
        )

        self.output_box.configure(
            state="disabled",
        )


    def update_status(self, text, progress):

        self.status.configure(
            text=f"Status: {text}",
            text_color=WHITE,
        )

        self.progress.set(progress)

        self.update_idletasks()


    def start_processing(self, message="Processing..."):

        self.is_processing = True

        self.set_processing_state(
            True
        )

        self.status.configure(
            text=f"Status: {message}",
            text_color=YELLOW,
        )

        self.progress.set(0.1)

        self.update_idletasks()


    def finish_processing(self):

        self.is_processing = False

        self.set_processing_state(
            False
        )

        self.status.configure(
            text="Status: Ready",
            text_color=WHITE,
        )

        self.progress.set(0)

        self.update_idletasks()


    def fake_loading(self):

        self.update_status(
            "Processing PDF...",
            0.2,
        )

        time.sleep(0.5)

        self.update_status(
            "Generating AI Response...",
            0.5,
        )

        time.sleep(0.5)

        self.update_status(
            "Saving Results...",
            0.8,
        )

        time.sleep(0.5)

        self.update_status(
            "Completed ✔",
            1.0,
        )

        time.sleep(0.3)

        self.update_status(
            "Ready",
            0,
        )


    def set_processing_state(self, processing=True):

        state = "disabled" if processing else "normal"

        # Main action buttons
        for button in self.left_frame.winfo_children():

            if isinstance(button, ctk.CTkButton):

                button.configure(
                    state=state
                )

        # Chat controls
        if hasattr(self, "chat_entry"):

            self.chat_entry.configure(
                state=state
            )

        if hasattr(self, "send_button"):

            self.send_button.configure(
                state=state
            )

    def run_summary(self):

        if not self.selected_pdf:
            self.show_output(
                "Please select a PDF first."
            )
            return

        self.start_processing(
            "Generating summary..."
        )

        def generate_summary():

            try:

                result = summarize_pdf(
                    self.selected_pdf
                )

                self.after(
                    0,
                    lambda: self.finish_summary(
                        result
                    ),
                )

            except Exception as error:

                self.after(
                    0,
                    lambda: self.finish_summary(
                        f"Summary Error:\n\n{error}"
                    ),
                )

        threading.Thread(
            target=generate_summary,
            daemon=True,
        ).start()


    def finish_summary(self, result):

        self.show_output(
            result
        )

        self.finish_processing()

    def open_quiz_settings(self):

        settings_window = ctk.CTkToplevel(self)

        settings_window.title("Quiz Settings")
        settings_window.geometry("400x350")
        settings_window.resizable(False, False)

        settings_window.transient(self)
        settings_window.grab_set()

        title = ctk.CTkLabel(
            settings_window,
            text="Quiz Settings",
            font=("Arial", 24, "bold"),
        )
        title.pack(pady=(30, 20))

        # Number of questions
        questions_label = ctk.CTkLabel(
            settings_window,
            text="Number of Questions",
            font=("Arial", 14),
        )
        questions_label.pack(pady=(5, 5))

        questions_menu = ctk.CTkOptionMenu(
            settings_window,
            values=["5", "10", "15"],
            width=200,
        )
        questions_menu.set("5")
        questions_menu.pack(pady=(0, 20))

        # Difficulty
        difficulty_label = ctk.CTkLabel(
            settings_window,
            text="Difficulty",
            font=("Arial", 14),
        )
        difficulty_label.pack(pady=(5, 5))

        difficulty_menu = ctk.CTkOptionMenu(
            settings_window,
            values=["Easy", "Medium", "Hard"],
            width=200,
        )
        difficulty_menu.set("Medium")
        difficulty_menu.pack(pady=(0, 25))

        def generate():

            num_questions = int(
                questions_menu.get()
            )

            difficulty = (
                difficulty_menu.get()
                .lower()
            )


            self.start_quiz(
                settings_window,
                num_questions,
                difficulty,
            )

        generate_button = ctk.CTkButton(
            settings_window,
            text="Generate Quiz",
            width=200,
            height=45,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            command=generate,
        )

        generate_button.pack(pady=10)


    def show_quiz(self, quiz_text):

        self.output_box.configure(
            state="normal"
        )

        self.output_box.delete(
            "1.0",
            "end",
        )

        self.output_box.insert(
            "end",
            quiz_text,
        )

        self.output_box.configure(
            state="disabled"
        )


    def run_quiz(self, num_questions, difficulty):

        if not self.selected_pdf:

            self.show_output(
                "Please select a PDF first."
            )

            return

        self.start_quiz(
            None,
            num_questions,
            difficulty,
        )

    def run_flashcards(self):

        if not self.selected_pdf:
            self.show_output(
                "Please select a PDF first."
            )
            return

        self.start_processing(
            "Generating flashcards..."
        )

        def generate_flashcards():

            try:

                result = flashcards_pdf(
                    self.selected_pdf
                )

                flashcards = parse_flashcards(
                    result
                )

                if not flashcards:

                    self.after(
                        0,
                        lambda: self.finish_flashcards_error(
                            "Could not parse the generated flashcards."
                        ),
                    )

                    return

                self.after(
                    0,
                    lambda: self.display_flashcards(
                        flashcards
                    ),
                )

            except Exception as error:

                self.after(
                    0,
                    lambda: self.finish_flashcards_error(
                        f"Flashcard Error:\n\n{error}"
                    ),
                )

        threading.Thread(
            target=generate_flashcards,
            daemon=True,
        ).start()


    def display_flashcards(self, flashcards):

        self.flashcards = flashcards

        self.flashcard_current_index = 0

        self.flashcard_answer_visible = False

        self.hide_output_area()

        self.quiz_frame.pack_forget()

        self.flashcard_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15,
        )

        self.display_flashcard()

        self.finish_processing()


    def finish_flashcards_error(self, message):

        self.show_output(
            message
        )

        self.finish_processing()

    def display_flashcard(self):

        if not self.flashcards:
            return

        card = self.flashcards[
            self.flashcard_current_index
        ]

        card_number = (
            self.flashcard_current_index + 1
        )

        total_cards = len(
            self.flashcards
        )

        self.flashcard_progress.configure(
            text=f"Card {card_number} of {total_cards}"
        )

        self.flashcard_question.configure(
            text=card["question"]
        )

        self.flashcard_answer.configure(
            text=""
        )

        self.flashcard_answer_visible = False

        self.flashcard_show_button.configure(
            text="Show Answer",
            state="normal",
            command=self.show_flashcard_answer,
        )

        self.flashcard_next_button.configure(
            text="Next Card",
            state="disabled",
        )


    def show_flashcard_answer(self):

        if not self.flashcards:
            return

        card = self.flashcards[
            self.flashcard_current_index
        ]

        self.flashcard_answer.configure(
            text=f"Answer:\n{card['answer']}"
        )

        self.flashcard_answer_visible = True

        self.flashcard_show_button.configure(
            text="Answer Revealed",
            state="disabled",
        )

        self.flashcard_next_button.configure(
            state="normal",
        )


    def next_flashcard(self):

        if not self.flashcards:
            return

        self.flashcard_current_index += 1

        if self.flashcard_current_index >= len(
            self.flashcards
        ):

            self.show_flashcard_result()

            return

        self.display_flashcard()


    def show_flashcard_result(self):

        total_cards = len(
            self.flashcards
        )

        self.flashcard_progress.configure(
            text="Flashcards Completed!"
        )

        self.flashcard_question.configure(
            text=f"You reviewed all {total_cards} flashcards."
        )

        self.flashcard_answer.configure(
            text="Great job! Keep reviewing your notes.",
        )

        self.flashcard_show_button.configure(
            text="Completed",
            state="disabled",
        )

        self.flashcard_next_button.configure(
            text="Review Again",
            state="normal",
            command=self.restart_flashcards,
        )

    def restart_flashcards(self):

        self.flashcard_current_index = 0
        self.flashcard_answer_visible = False

        self.flashcard_next_button.configure(
            text="Next Card",
            state="disabled",
            command=self.next_flashcard,
        )

        self.flashcard_show_button.configure(
            text="Show Answer",
            state="normal",
            command=self.show_flashcard_answer,
        )

        self.display_flashcard()


    def run_chat(self):

        if not self.selected_pdf:
            self.show_output(
                "Please select a PDF first."
            )
            return

        question = self.chat_entry.get().strip()

        if not question:
            return

        # Disable input while AI is working
        self.chat_entry.configure(
            state="disabled"
        )

        self.send_button.configure(
            state="disabled"
        )

        self.update_status(
            "Generating AI response...",
            0.5,
        )

        def generate_answer():

            try:

                result = chat_pdf(
                    self.selected_pdf,
                    question,
                )

                self.after(
                    0,
                    lambda: self.finish_chat(
                        question,
                        result,
                    ),
                )

            except Exception as error:

                self.after(
                    0,
                    lambda: self.finish_chat(
                        question,
                        f"Chat Error:\n\n{error}",
                    ),
                )

        threading.Thread(
            target=generate_answer,
            daemon=True,
        ).start()


    def finish_chat(self, question, answer):

        self.output_box.configure(
            state="normal"
        )

        self.output_box.insert(
            "end",
            f"\n\nYou:\n{question}\n"
        )

        self.output_box.insert(
            "end",
            f"\nAI:\n{answer}\n"
        )

        self.output_box.see("end")

        self.output_box.configure(
            state="disabled"
        )

        self.chat_entry.configure(
            state="normal"
        )

        self.send_button.configure(
            state="normal"
        )

        self.chat_entry.delete(
            0,
            "end",
        )

        self.chat_entry.focus_set()

        self.update_status(
            "Ready",
            0,
        )

    def open_results_folder(self):

        results_path = os.path.join(
            os.getcwd(),
            "results",
        )

        if os.path.exists(results_path):
            subprocess.Popen(f'explorer "{results_path}"')
        else:
            self.show_output("Results folder does not exist yet.")


    def clear_chat(self):

        # Clear chat history for the selected PDF
        if self.selected_pdf:
            chat_history.pop(
                self.selected_pdf,
                None
            )

        # Clear output box
        self.output_box.configure(
            state="normal"
        )

        self.output_box.delete(
            "1.0",
            "end",
        )

        self.output_box.insert(
            "end",
            "Chat cleared.\n"
        )

        self.output_box.configure(
            state="disabled"
        )


    def answer_quiz(self, selected_option):

        if not self.quiz_questions:
            return

        question = self.quiz_questions[
            self.quiz_current_index
        ]

        correct_answer = question["answer"]

        # Disable all options after answering
        for button in self.quiz_option_buttons.values():
            button.configure(
                state="disabled"
            )

        if selected_option == correct_answer:

            self.quiz_score += 1

            self.quiz_option_buttons[
                selected_option
            ].configure(
                fg_color="#1F7A3D"
            )

        else:

            self.quiz_option_buttons[
                selected_option
            ].configure(
                fg_color="#8B1E1E"
            )

            self.quiz_option_buttons[
                correct_answer
            ].configure(
                fg_color="#1F7A3D"
            )

        self.quiz_explanation.configure(
            text=(
                "Explanation:\n"
                + question.get(
                    "explanation",
                    ""
                )
            )
        )


    def next_quiz_question(self):

        if not self.quiz_questions:
            return

        self.quiz_current_index += 1

        if self.quiz_current_index >= len(
            self.quiz_questions
        ):

            self.show_quiz_result()

            return

        self.display_quiz_question()


    def display_quiz_question(self):

        question = self.quiz_questions[
            self.quiz_current_index
        ]

        question_number = (
            self.quiz_current_index + 1
        )

        total_questions = len(
            self.quiz_questions
        )

        self.quiz_progress.configure(
            text=f"Question {question_number} of {total_questions}"
        )

        self.quiz_question.configure(
            text=question["question"]
        )

        for option in ["A", "B", "C", "D"]:

            self.quiz_option_buttons[
                option
            ].configure(
                text=f"{option}) {question['options'][option]}",
                state="normal",
                fg_color=NAVY,
            )

        self.quiz_explanation.configure(
            text=""
        )

        self.quiz_next_button.configure(
            text="Next Question"
        )

    def show_quiz_result(self):

        total_questions = len(self.quiz_questions)

        if total_questions == 0:
            return

        correct_answers = self.quiz_score
        wrong_answers = total_questions - correct_answers

        percentage = int(
            (correct_answers / total_questions) * 100
        )

        # -----------------------------
        # Quiz Completed
        # -----------------------------

        self.quiz_progress.configure(
            text="Quiz Completed!",
            text_color=YELLOW,
            font=("Arial", 18, "bold"),
        )

        # -----------------------------
        # Result Message
        # -----------------------------

        if percentage >= 80:
            message = "Excellent work! 🎉"

        elif percentage >= 60:
            message = "Good job! Keep practicing. 👍"

        else:
            message = "Keep studying and try again. 💪"

        self.quiz_question.configure(
            text=(
                f"Your Score\n\n"
                f"{correct_answers} / {total_questions}\n\n"
                f"Accuracy: {percentage}%\n\n"
                f"{message}"
            ),
            font=("Arial", 24, "bold"),
            justify="center",
        )

        # -----------------------------
        # Hide Answer Buttons
        # -----------------------------

        for button in self.quiz_option_buttons.values():
            button.pack_forget()

        # -----------------------------
        # Result Statistics
        # -----------------------------

        self.quiz_explanation.configure(
            text=(
                f"Correct Answers: {correct_answers}\n"
                f"Wrong Answers: {wrong_answers}"
            ),
            font=("Arial", 14),
            justify="center",
        )

        # -----------------------------
        # Try Again
        # -----------------------------

        self.quiz_next_button.configure(
            text="Try Again",
            command=self.restart_quiz,
            fg_color=YELLOW,
            hover_color=YELLOW_HOVER,
            text_color=BLACK,
        )


    def restart_quiz(self):

        self.quiz_current_index = 0
        self.quiz_score = 0

        self.quiz_next_button.configure(
            text="Next Question",
            command=self.next_quiz_question,
        )

        for button in self.quiz_option_buttons.values():
            button.pack(
                fill="x",
                padx=40,
                pady=6,
            )

        self.display_quiz_question()

if __name__ == "__main__":
    app = AIStudyAssistantGUI()
    app.mainloop()

