import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text = "Click me", fg = "red", command = lambda : print("Hello World"))
button.pack(side = tk.LEFT)
root.mainloop()
