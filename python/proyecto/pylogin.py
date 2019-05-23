import hashlib

from tkinter import Tk, Label, Entry, GROOVE, Button
from tkinter import messagebox
from db import loginDB, registerUser, closeDB

__BGCLR="#282828"
__FGCLR="#cecece"
__CLR='#004a95'
__FGCOLOR='white'
__GEOMETRY="420x400"
__TITLE="Login GUI"
__FONT_PASS=("blod",14)
__WIDTH=40
__FONT=10
__LABEL_X=20
__LABEL_Y=50
__LABEL_PASS_X=20
__LABEL_PASS_Y=130
__USER_X=20
__USER_Y=80
__PASS_X=20
__PASS_Y=160
__BD=5
__WARN_LABEL_X=80
__WARN_LABEL_Y=200
__BUTTOM_LOGIN_X=20
__BUTTOM_LOGIN_Y=240
__BUTTOM_REG_X=20
__BUTTOM_REG_Y=300
__HIGHLIGHT_LETTER=2
__HIGHLIGHT_BOTTOM=4


def login():

    seed = password_Entry.get()
    h = hashlib.sha256(seed.encode())
    
    access = loginDB(user_Entry.get(), h.hexdigest())

    if access:
        messagebox.showinfo('Login', 'Login correcto!')
        user_Entry.delete(0, 'end')
        password_Entry.delete(0, 'end')
    else:
        warn.config(text="Invalid username or Password",fg="red")
        user_Entry.delete(0, 'end')
        password_Entry.delete(0, 'end')

def register():

    seed = password_Entry.get()
    h = hashlib.sha256(seed.encode())

    check = registerUser(user_Entry.get(), h.hexdigest())

    if check:
        messagebox.showinfo('Registro', 'Registro efectuado')
        user_Entry.delete(0, 'end')
        password_Entry.delete(0, 'end')
    else:
        messagebox.showinfo('Registro', 'El usuario ya existe')
        user_Entry.delete(0, 'end')
        password_Entry.delete(0, 'end')

w=Tk()
w.title(__TITLE)
w.geometry(__GEOMETRY)
w.config(bg=__BGCLR)
w.resizable(False, False)

user=Label(w,
            text="User",
            font=(__FONT_PASS),
            bg=__BGCLR,
            fg=__FGCLR)
user.place(x=__LABEL_X,y=__LABEL_Y)

user_Entry=Entry(w,bg=__BGCLR,
            fg=__FGCOLOR,
            relief=GROOVE,
            highlightcolor=__FGCOLOR,
            highlightthickness=__HIGHLIGHT_LETTER,
            highlightbackground=__CLR,
            width=__WIDTH,
            font=__FONT,
            bd=__BD)
user_Entry.place(x=__USER_X,y=__USER_Y)

password=Label(w,
            text="Password",
            font=(__FONT_PASS),
            bg=__BGCLR,
            fg=__FGCLR)
password.place(x=__LABEL_PASS_X,y=__LABEL_PASS_Y)

password_Entry=Entry(w,bg=__BGCLR,
            fg=__FGCOLOR,
            relief=GROOVE,
            highlightcolor=__FGCOLOR,
            highlightthickness=__HIGHLIGHT_LETTER,
            highlightbackground=__CLR, 
            width=__WIDTH,
            font=__FONT,
            show="*",
            bd=__BD)
password_Entry.place(x=__PASS_X,y=__PASS_Y)

warn=Label(w,
            font=("blod",10),
            bg=__BGCLR)
           
warn.place(x=__WARN_LABEL_X,y=__WARN_LABEL_Y)

button=Button(w,
            text="Login",
            bg=__CLR,
            fg=__FGCOLOR,
            relief=GROOVE,
            highlightcolor=__CLR,
            highlightthickness=__HIGHLIGHT_BOTTOM,
            width=__WIDTH,
            font=__FONT,
            command=login)
button.place(x=__BUTTOM_LOGIN_X,y=__BUTTOM_LOGIN_Y)

button=Button(w,
            text="Register",
            bg=__CLR,
            fg=__FGCOLOR,
            relief=GROOVE,
            highlightcolor=__CLR,
            highlightthickness=__HIGHLIGHT_BOTTOM,
            width=__WIDTH,
            font=__FONT,
            command=register)
button.place(x=__BUTTOM_REG_X,y=__BUTTOM_REG_Y)


if __name__ == "__main__":
    try:
        w.mainloop()

    finally:
        closeDB()
