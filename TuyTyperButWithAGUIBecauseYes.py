import tkinter as tk
import time
import threading
import pyautogui

class AutoTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typer")
        self.running = False

        self.delay_label = tk.Label(root, text="Delay (seconds):")
        self.delay_entry = tk.Entry(root)
        self.text_label = tk.Label(root, text="Text to type:")
        self.text_entry = tk.Entry(root)
        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing)
        self.stop_button = tk.Button(root, text="Stop Typing", command=self.stop_typing)

        self.delay_label.pack(pady=5)
        self.delay_entry.pack(pady=5)
        self.text_label.pack(pady=5)
        self.text_entry.pack(pady=5)
        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)

    def start_typing(self):
        if not self.running:
            self.running = True
            self.delay = float(self.delay_entry.get())
            self.text_to_type = self.text_entry.get()
            self.typing_thread = threading.Thread(target=self.auto_type)
            self.typing_thread.start()

    def stop_typing(self):
        self.running = False

    def auto_type(self):
        try:
            while self.running:
                pyautogui.typewrite(self.text_to_type)
                pyautogui.press("enter")
                time.sleep(self.delay)
    
        except Exception as e:
            print("Error:", e)
            self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyperApp(root)
    root.mainloop()
