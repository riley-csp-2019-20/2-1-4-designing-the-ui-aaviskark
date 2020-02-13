##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x125")
root.title("authentication")

# create empty frame
frame_login = tk.Frame(root)

frame_login.grid()
lbl_username = tk.Label(frame_login, text='Username:', font = "Courier")
lbl_username.pack()

lbl_password= tk.Label(frame_login,text="Password:",font="Courier")
lbl_password.pack(pady = 25)
lbl_password.pack(padx = 25)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=1)

def callback():
    print(root.get())

btn_login = tk.Button(root, text="Log In", width=10, command=callback)


root.mainloop()