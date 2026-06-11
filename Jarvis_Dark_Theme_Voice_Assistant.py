
import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random
import webbrowser

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis Voice Assistant")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e1e")

        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)

        self.running = False

        title = tk.Label(
            root,
            text="JARVIS VOICE ASSISTANT",
            font=("Arial", 18, "bold"),
            bg="#1e1e1e",
            fg="cyan"
        )
        title.pack(pady=10)

        self.status = tk.Label(
            root,
            text="Status: Ready",
            font=("Arial", 12),
            bg="#1e1e1e",
            fg="white"
        )
        self.status.pack()

        self.chat = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            bg="#2b2b2b",
            fg="white",
            font=("Consolas", 11)
        )
        self.chat.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(
            btn_frame,
            text="Start Listening",
            command=self.start_listening,
            width=18
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = tk.Button(
            btn_frame,
            text="Stop",
            command=self.stop_listening,
            width=18
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

        self.write("Assistant", "Dark Theme Voice Assistant Ready!")

    def write(self, sender, msg):
        self.chat.insert(tk.END, f"{sender}: {msg}\n")
        self.chat.see(tk.END)

    def speak(self, text):
        self.write("Assistant", text)
        self.engine.say(text)
        self.engine.runAndWait()

    def start_listening(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.listen_loop, daemon=True).start()

    def stop_listening(self):
        self.running = False
        self.status.config(text="Status: Stopped")

    def listen_loop(self):
        while self.running:
            try:
                self.status.config(text="Status: Listening...")

                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = self.recognizer.listen(source, timeout=10)

                self.status.config(text="Status: Processing...")

                command = self.recognizer.recognize_google(audio).lower()
                self.write("You", command)

                self.process_command(command)

            except Exception:
                pass

    def process_command(self, command):

        if "time" in command:
            self.speak(datetime.now().strftime("Current time is %I:%M %p"))

        elif "date" in command:
            self.speak(datetime.now().strftime("Today is %A %d %B %Y"))

        elif "joke" in command:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything.",
                "What do you call a fake noodle? An impasta."
            ]
            self.speak(random.choice(jokes))

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                self.speak(f"Searching for {query}")

        elif any(x in command for x in ["bye", "exit", "quit", "stop"]):
            self.speak("Goodbye!")
            self.running = False

        else:
            self.speak("I did not understand that command.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()
