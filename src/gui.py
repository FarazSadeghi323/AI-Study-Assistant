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
            command=lambda: threading.Thread(
                target=self.run_summary,
                daemon=True,
            ).start(),
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="📝 Generate Quiz",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=lambda: threading.Thread(
                target=self.run_quiz,
                daemon=True,
            ).start(),
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="🗂 Generate Flashcards",
            width=button_width,
            height=button_height,
            fg_color=NAVY,
            hover_color=NAVY_HOVER,
            text_color=WHITE,
            command=lambda: threading.Thread(
                target=self.run_flashcards,
                daemon=True,
            ).start(),
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

        output_title = ctk.CTkLabel(
            self.right_frame,
            text="Output",
            font=("Arial", 18, "bold"),
            text_color=WHITE,
        )

        output_title.pack(
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

        chat_frame = ctk.CTkFrame(
            self.right_frame,
            corner_radius=10,
        )  

        chat_frame.pack(
            fill="x",
            padx=15,
            pady=(0, 15),
        )

        chat_frame.grid_columnconfigure(
            0,
            weight=1,
        )

        # -----------------------------
        # Chat Entry
        # -----------------------------

        self.chat_entry = ctk.CTkEntry(
            chat_frame,
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
            chat_frame,
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
            chat_frame,
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

        question = self.chat_entry.get().strip()

        if not question:
            return

        # -----------------------------
        # Show User Question
        # -----------------------------

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
        self.update_idletasks()

        # -----------------------------
        # Ask AI
        # -----------------------------

        answer = chat_pdf(
            self.selected_pdf,
            question
        )

        # -----------------------------
        # Show AI Answer
        # -----------------------------

        self.output_box.insert(
            "end",
            f"\nAI:\n{answer}\n"
        )

        self.output_box.see("end")

        # -----------------------------
        # Lock Output
        # -----------------------------

        self.output_box.configure(
            state="disabled"
        )

        # -----------------------------
        # Clear Input
        # -----------------------------

        self.chat_entry.delete(
            0,
            "end"
        )

        # Return focus to chat input
        self.chat_entry.focus_set()


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

    def run_summary(self):

        if not self.selected_pdf:
            self.show_output("Please select a PDF first.")
            return

        self.fake_loading()

        result = summarize_pdf(self.selected_pdf)

        self.show_output(result)


    def run_quiz(self):

        if not self.selected_pdf:
            self.show_output("Please select a PDF first.")
            return

        self.fake_loading()

        result = quiz_pdf(self.selected_pdf)
        
        self.show_output(result)

    def run_flashcards(self):

        if not self.selected_pdf:
            self.show_output("Please select a PDF first.")
            return

        self.fake_loading()

        result = flashcards_pdf(self.selected_pdf)

        self.show_output(result)

    def run_chat(self):

        if not self.selected_pdf:
            self.show_output(
                "Please select a PDF first."
            )
            return

        question = self.chat_entry.get().strip()

        if not question:
            return

        self.fake_loading()

        result = chat_pdf(
            self.selected_pdf,
            question,
        )

        self.show_output(result)

        self.chat_entry.delete(
            0,
            "end",
        )

        self.chat_entry.focus_set()

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
    
if __name__ == "__main__":
    app = AIStudyAssistantGUI()
    app.mainloop()
    