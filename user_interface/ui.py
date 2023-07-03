```python
import tkinter as tk
from tkinter import messagebox

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Model Talk AI")
        self.root.geometry("800x600")

        self.chat_window = tk.Text(self.root, bd=1, padx=5, width=50, height=8)
        self.chat_window.place(x=20, y=20)

        self.message_entry = tk.Entry(self.root, bd=1, width=40)
        self.message_entry.place(x=20, y=550)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, width=10, height=2)
        self.send_button.place(x=680, y=540)

    def send_message(self):
        message = self.message_entry.get()
        self.chat_window.insert(tk.END, "You: " + message + "\n")
        self.message_entry.delete(0, tk.END)

        # TODO: Implement message handling and response generation here

    def display_message(self, message):
        self.chat_window.insert(tk.END, "Model Talk AI: " + message + "\n")

    def display_error(self, error_message):
        messagebox.showerror("Error", error_message)

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
```