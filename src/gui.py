import customtkinter as ctk

from main import (
    summarize_pdf,
    quiz_pdf,
    flashcards_pdf,
    chat_pdf,
)
import threading
import time

# Theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AIStudyAssistantGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("AI Study Assistant")
        self.geometry("700x580")
        self.resizable(False, False)

        title = ctk.CTkLabel(
            self,
            text="AI Study Assistant",
            font=("Arial", 28, "bold"),
        )
        title.pack(pady=30)

        subtitle = ctk.CTkLabel(
            self,
            text="Your AI-powered PDF learning assistant",
            font=("Arial", 16),
        )
        subtitle.pack(pady=5)

        self.status = ctk.CTkLabel(
            self,
            text="Status: Ready",
            font=("Arial", 14),
        )
        self.status.pack(pady=10)

        self.progress = ctk.CTkProgressBar(
            self,
            width=350,
        )
        self.progress.pack(pady=10)
        self.progress.set(0)

        self.create_buttons()

    def update_status(self, text, progress):
        self.status.configure(text=f"Status: {text}")
        self.progress.set(progress)
        self.update_idletasks()

    def fake_loading(self):
        self.update_status("Processing PDF...", 0.2)
        time.sleep(0.5)

        self.update_status("Generating AI Response...", 0.5)
        time.sleep(0.5)

        self.update_status("Saving Results...", 0.8)
        time.sleep(0.5)

        self.update_status("Completed ✔", 1.0)

    def run_summary(self):
        self.fake_loading()
        summarize_pdf()
        self.update_status("Ready", 0)

    def create_buttons(self):

        button_width = 260
        button_height = 45

        ctk.CTkButton(
            self,
            text="📄 Summarize PDF",
            width=button_width,
            height=button_height,
            command=lambda: threading.Thread(
                target=self.run_summary,
                daemon=True,
            ).start(),
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="📝 Generate Quiz",
            width=button_width,
            height=button_height,
            command=quiz_pdf,
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="🗂 Generate Flashcards",
            width=button_width,
            height=button_height,
            command=flashcards_pdf,
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="💬 Chat with Notes",
            width=button_width,
            height=button_height,
            command=chat_pdf,
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="🚪 Exit",
            width=button_width,
            height=button_height,
            command=self.destroy,
        ).pack(pady=30)


if __name__ == "__main__":
    app = AIStudyAssistantGUI()
    app.mainloop()