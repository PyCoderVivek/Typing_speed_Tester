import tkinter as tk
import time

class TypingSpeedTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")

        self.text_to_type = "This is a typing speed test. Type this as fast as you can!"
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Typing Test", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def start_test(self):
        self.start_time = time.time()
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.text_to_type)
        self.entry.bind("<Return>", self.check_speed)
        self.start_button.config(state=tk.DISABLED)

    def check_speed(self, event):
        typed_text = self.entry.get()
        end_time = time.time()
        time_taken = end_time - self.start_time
        words_per_minute = (len(typed_text.split()) / time_taken) * 60

        self.result_label.config(text=f"Your typing speed: {words_per_minute:.2f} words per minute")
        self.entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)
        self.entry.unbind("<Return>")

if __name__ == "__main__":
    root = tk.Tk()
    typing_speed_tester = TypingSpeedTester(root)
    root.mainloop()
