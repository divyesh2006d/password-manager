from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

def generate_password():
    password = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*") for _ in range(12))
    inp_passw.delete(0, END)   # clear old password
    inp_passw.insert(0, password)
    window.clipboard_clear()   # copy to clipboard automatically
    window.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    # messagebox.showinfo('Info', 'Password has been saved.')

    if len(inp_web.get()) != 0 and len(inp_passw.get()) != 0:
        messagebox.askokcancel(title= f'{inp_web.get()}', message=f'These are the details entered :\n Email : {inp_email.get()}\n'
                                                  f'Password : {inp_passw.get()} \n it is ok to save ?')
    else:
        messagebox.showerror('Error', 'Something went wrong.')

    with open('password.txt', 'a') as file:
        file.write(f'{inp_web.get()},{inp_email.get()},{inp_passw.get()}\n')
    inp_web.delete(0, END)
    inp_passw.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=10, pady=10)

image = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100,100,image=image)
canvas.grid(row=0, column=1)

# labels
web = Label(window, text='Website :')
web.grid(row=1, column=0)

email = Label(window, text='Email/Username :')
email.grid(row=2, column=0)

passw = Label(window, text='Password :')
passw.grid(row=3, column=0)

# inputs
inp_web = Entry(width=52)
inp_web.grid(row=1, column=1, columnspan=2)
inp_web.focus()

inp_email = Entry(width=52)
inp_email.grid(row=2, column=1,columnspan=2)
inp_email.insert(0,'divyesh@gmail.com')

inp_passw = Entry(width=34)
inp_passw.grid(row=3, column=1,columnspan=1)


# butten
G_btn = Button(text='Generate Password', command=generate_password)
G_btn.grid(row=3, column=2)

add_btn = Button(text='Add Password', command=save,width=44)
add_btn.grid(row=4, column=1,columnspan=2)

window.mainloop()