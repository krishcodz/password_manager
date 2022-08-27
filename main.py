import json
from logging import exception
from tkinter import *
import random
from tkinter import messagebox

YOUREMAIL ="enter your email here"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password_generated = ""
    for char in password_list:
        password_generated += char

    password_entry.insert(index=0, string=password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    t1 = website_entry.get()
    t2 = email_entry.get()
    t3 = password_entry.get()
    t = t1 + ' | ' + t2 + ' | ' + t3 + '\n'
    if len(t1) == 0 or len(t2) == 0 or len(t3) == 0:
        messagebox.showerror(title='ERROR', message='do not leave any fields blank')
        return None
    is_ok = messagebox.askokcancel(title='Detail',
                                   message=f'entered details are\n website:{t1}\nemail/username:{t2}\npassword:{t3}\n\n\n press "ok" to proceed')
    if is_ok:
        new_data = {
            t1: {
                "email":t2,
                "password":t3,
            }
        }

        try:
            with open('saved_passwords.json', 'r') as f:
                data = json.load(f)
                data.update(new_data)
        except:
            with open('saved_passwords.json', 'w') as f:
                json.dump(new_data, f, indent=4)
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

        else:
            with open('saved_passwords.json', 'r') as f:
                data = json.load(f)
                data.update(new_data)
            
            with open('saved_passwords.json', 'w') as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------FIND PASSWORD------------------------------#

def find_password():
    website_data = website_entry.get()
    try:
        with open('saved_passwords.json', 'r') as f:
            data = json.load(f)
            
    except:
        messagebox.showerror(title='ERROR', message='No Data Found')
    else:
        if website_data in data:
            messagebox.showinfo(title='Details', message=f'Website:{website_data}\n Password:{data[website_data]["password"]}')
        else:
            messagebox.showerror(title='Error', message="Details not found")
        
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
# labels

website = Label(text='Website')
email = Label(text='Email/Username')
password = Label(text='Password')
website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)

# entry

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(index=0, string=YOUREMAIL)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# buttons
generate_pass = Button(text='Generate password', command=generate_password)
generate_pass.grid(column=2, row=3)

add_button = Button(text='Add', width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search = Button(text="search",command=find_password, width=15)
search.grid(row=1,column=2)

window.mainloop()
