from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
window.config(padx=20, pady=20)

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

# butten
G_btn = Button(text='Generate Password', command=generate_password)
G_btn.grid(row=3, column=2)

add_btn = Button(text='Add Password', command=save,width=36)
add_btn.grid(row=4, column=1,columnspan=2)

# inputs
inp_web = Entry(width=35)
inp_web.grid(row=1, column=1, columnspan=2)
inp_web.focus()

inp_email = Entry(width=35)
inp_email.grid(row=2, column=1,columnspan=2)
inp_email.insert(0,'divyesh@gmail.com')

inp_passw = Entry(width=21)
inp_passw.grid(row=3, column=1)

window.mainloop()