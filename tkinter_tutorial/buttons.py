import tkinter as tk

root = tk.Tk()

def my_click():
     label = tk.Label(root, text="Look!, I clicked a Button!!")
     label.pack()

button1 = tk.Button(root, text="Click Me!", command=my_click, bg="brown", fg="white")
button1.pack()

root.mainloop()