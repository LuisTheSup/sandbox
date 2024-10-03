import tkinter as tk

root = tk.Tk()

# Creating a Label widget
label1 = tk.Label(root, text="Hello World!")
label2 = tk.Label(root, text="My Name is John Elder")
 
# Shoving it onto the screen
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

root.mainloop()
