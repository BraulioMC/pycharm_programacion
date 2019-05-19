from tkinter import *
from tkinter import messagebox
from db import loginDB, registerUser, closeDB

bgclr="#282828"
fgclr="#cecece"
clr='#004a95'

def login():

    access = loginDB(user_Entry.get(), password_Entry.get())

    if access:
        messagebox.showinfo('Login', 'Login correcto!')
        w.destroy()
    else:
        warn.config(text="Invalid username or Password",fg="red")

def register():
    check = registerUser(user_Entry.get(),password_Entry.get())

    if check:
        messagebox.showinfo('Registro', 'Registro efectuado')
    else:
        messagebox.showinfo('Registro', 'El usuario ya existe')

w=Tk()
w.title("Login GUI")
w.geometry("420x400")
w.config(bg=bgclr)
w.resizable()

user=Label(w,
            text="User",
            font=("blod",15),
            bg=bgclr,
            fg=fgclr)
user.place(x=20,y=40)

user_Entry=Entry(w,bg=bgclr,
            fg="white",
            relief=GROOVE,
            highlightcolor="white",
            highlightthickness=2,
            highlightbackground=clr,
            width=40,
            font=10,
            bd=5)
user_Entry.place(x=20,y=80)

password=Label(w,
            text="Password",
            font=("blod",15),
            bg=bgclr,
            fg=fgclr)
password.place(x=20,y=120)

password_Entry=Entry(w,bg=bgclr,
            fg="white",
            relief=GROOVE,
            highlightcolor="white",
            highlightthickness=2,
            highlightbackground=clr, 
            width=40,
            font=10,
            show="*",
            bd=5)
password_Entry.place(x=20,y=160)

warn=Label(w,
            font=("blod",10),
            bg=bgclr)
           
warn.place(x=80,y=200)

button=Button(w,
            text="Login",
            bg=clr,
            fg="white",
            relief=GROOVE,
            highlightcolor=clr,
            highlightthickness=4,
            width=40,
            font=10,
            command=login)
button.place(x=20,y=240)

button=Button(w,
            text="Register",
            bg=clr,
            fg="white",
            relief=GROOVE,
            highlightcolor=clr,
            highlightthickness=4,
            width=40,
            font=10,
            command=register)
button.place(x=20,y=300)

if __name__ == "__main__":
    try:
        w.mainloop()

    finally:
        closeDB()
