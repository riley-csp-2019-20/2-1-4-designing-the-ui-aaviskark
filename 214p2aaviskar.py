import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

bluebox = tk.Canvas(root, width= 100, height = 100, bg = "blue")
bluebox.grid(row = 0, column = 0)

greenbox = tk.Canvas(root, width=100, height = 100, bg= "green")
greenbox.grid(row=0, column = 1)

redbox = tk.Canvas(root, width = 100, height = 100, bg = "red")
redbox.grid(row = 1, column = 0)

yellowbox = tk.Canvas(root, width = 100, height = 100, bg = "yellow")
yellowbox.grid(row = 1, column = 1)


root.mainloop()