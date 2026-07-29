import threading
import time

import customtkinter as ctk

from tkinter.scrolledtext import ScrolledText

from main import (
    summarize_pdf,
    quiz_pdf,
    flashcards_pdf,
    chat_pdf,
)

# -----------------------------
# Theme
# -----------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AIStudyAssistantGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Window
        # -----------------------------
        self.title("AI Study Assistant")
        self.geometry("1000x650")
        self.minsize(1000, 650)

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

    def create_header(self):
        title = ctk.CTkLabel(
            self,
            text="AI Study Assistant",
            font=("Arial", 30, "bold"),
        )

        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Your AI-powered PDF learning assistant",
            font=("Arial", 16),
        )

        subtitle.pack()

    def create_status_bar(self):
        self.status = ctk.CTkLabel(
            self,
            text="Status: Ready",
            font=("Arial", 15),
        )

        self.status.pack(pady=(20, 5))

        self.progress = ctk.CTkProgressBar(
            self,
            width=500,
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

        self.left_frame = ctk.CTkFrame(self.main_frame)

        self.left_frame.grid(
            row=0,
            column=0,
            sticky="nswe",
            padx=(10, 5),
            pady=10,
        )

        self.right_frame = ctk.CTkFrame(self.main_frame)

        self.right_frame.grid(
            row=0,
            column=1,
            sticky="nswe",
            padx=(5, 10),
            pady=10,
        )

    def create_footer(self):
        footer = ctk.CTkLabel(
            self,
            text="© AI Study Assistant",
            font=("Arial", 12),
        )

        footer.pack(pady=(0, 10))

    def create_buttons(self):
        button_width = 220
        button_height = 45

        ctk.CTkButton(
            self.left_frame,
            text="📄 Summarize PDF",
            width=button_width,
            height=button_height,
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
            command=lambda: threading.Thread(
                target=quiz_pdf,
                daemon=True,
            ).start(),
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="🗂 Generate Flashcards",
            width=button_width,
            height=button_height,
            command=lambda: threading.Thread(
                target=flashcards_pdf,
                daemon=True,
            ).start(),
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="💬 Chat with Notes",
            width=button_width,
            height=button_height,
            command=lambda: threading.Thread(
                target=chat_pdf,
                daemon=True,
            ).start(),
        ).pack(pady=12, padx=15)

        ctk.CTkButton(
            self.left_frame,
            text="🚪 Exit",
            width=button_width,
            height=button_height,
            fg_color="#B22222",
            hover_color="#8B0000",
            command=self.destroy,
        ).pack(pady=(30, 15), padx=15)

    def create_output_box(self):
        output_title = ctk.CTkLabel(
            self.right_frame,
            text="Output",
            font=("Arial", 18, "bold"),
        )

        output_title.pack(
            pady=(15, 10),
        )

        self.output_box = ScrolledText(
            self.right_frame,
            wrap="word",
            font=("Consolas", 11),
        )

        self.output_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15),
        )

        self.output_box.insert(
            "end",
            "Welcome to AI Study Assistant.\n\n"
            "Choose one of the options from the left panel.",
        )

        self.output_box.configure(
            state="disabled",
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
            text=f"Status: {text}"
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

        self.fake_loading()

        summarize_pdf()

        self.show_output(
            "Summary has been generated successfully.\n\n"
            "The summary has also been saved in the results folder."
        )

    
if __name__ == "__main__":
    app = AIStudyAssistantGUI()
    app.mainloop()
    