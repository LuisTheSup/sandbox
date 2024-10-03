import tkinter as tk

class SimpleGUI:

    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry(f"{self.window.winfo_screenmmwidth()}x{self.window.winfo_screenheight()}")
        self.window.title("Simple Window")

        self.label = tk.Label(self.window, text="Cosmetology", font=("Helvetica", 18))
        self.label.pack()

        # Buttons
        self.button1 = tk.Button(self.window, text="Click Me!", font=("Helvetica", 12))
        self.button1.pack(pady=50)

        self.window.mainloop()


gui = SimpleGUI()