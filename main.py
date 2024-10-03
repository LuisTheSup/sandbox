import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.window = tk.Tk()

        self.label = tk.Label(self.window, text="Welcome!", font=("Helvetica", 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.window, height=5, font=("Helvetica", 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.window, text="Show Message", font=("Helvetica", 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.window, text="Show Message", font=("Helvetica", 18), command=self.show_message)
        self.button.pack()

        self.window.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))


my_gui = MyGUI()