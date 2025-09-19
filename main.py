from tkinter import *
from tkinter import messagebox
import json
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
    website = inp_web.get()
    emails = inp_email.get()
    password = inp_passw.get()

    new_data = {
        website: {
            'email': emails,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave Website or Password empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {emails}\nPassword: {password}\nIs it ok to save?"
        )

        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file,indent=4)
            else:
                data.update(new_data)

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                inp_web.delete(0, END)
                inp_passw.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = inp_web.get()
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File found.")
    else:
        if website in data:
            emails = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website,
                                   message=f'Email: {emails}\nPassword: {password}')
        else:
            messagebox.showwarning(title='oops..', message=f'{website} is not found')
    finally:
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
G_btn = Button(text='Generate Password', command=generate_password,bg='green')
G_btn.grid(row=3, column=2)

add_btn = Button(text='Add Password', command=save,width=44,bg='blue')
add_btn.grid(row=4, column=1,columnspan=2)

search_btn = Button(text='Search ', command=find_password,width=14,bg='green')
search_btn.grid(row=1, column=2,columnspan=2)

window.mainloop()