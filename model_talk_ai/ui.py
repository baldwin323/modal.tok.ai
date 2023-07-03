```python
from tkinter import Tk, Text, Button, END, Scrollbar, Y

class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Model Talk AI")

        self.chatInput = Text(self.window, bd=3, height="5", width="50", font="Arial")
        self.chatInput.insert(END, "Type your message here...")
        self.chatInput.grid(row=1, column=0, columnspan=2)

        self.sendButton = Button(self.window, text="Send", width="20", height="5", bd=0, bg="#0080ff", activebackground="#00bfff",fg='#ffffff', command=self.send_message)
        self.sendButton.grid(row=1, column=2)

        self.scrollbar = Scrollbar(self.window)
        self.messageList = Text(self.window, width=50, height=15, yscrollcommand=self.scrollbar.set, state='disabled')
        self.messageList.grid(row=0, column=0, columnspan=3)
        self.scrollbar.grid(row=0, column=3, sticky=Y)

    def send_message(self):
        message = self.chatInput.get("1.0", 'end-1c').strip()
        self.chatInput.delete("0.0", END)
        if message != '':
            self.messageList.configure(state='normal')
            self.messageList.insert(END, "You: " + message + '\n')
            self.messageList.configure(state='disabled')

    def receive_message(self, message):
        self.messageList.configure(state='normal')
        self.messageList.insert(END, "Bot: " + message + '\n')
        self.messageList.configure(state='disabled')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UI()
    ui.run()
```