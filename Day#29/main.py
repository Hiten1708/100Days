from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# -------------------------------------------------- PASSWORD SEARCHER --------------------------------------------- #


def pass_search():
    try:
        with open("data.json") as filu:
            data = json.load(filu)
    except KeyError as er:
        messagebox.showerror(title="Error Occurred", message=f"Key: {er} does not exist")
    except FileNotFoundError as fr:
        messagebox.showerror(title="Error Occurred", message=f"File: {fr} does not exist")
    else:
        messagebox.showinfo(title="Your Info", message=f'Email: {data[web_ent.get()]["Email"]}\n '
                                                       f'Password:{data[web_ent.get()]["Password"]}')



# -------------------------------------------------- PASSWORD GENERATOR --------------------------------------------- #

def passwrd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_lt = [random.choice(letters) for char in range(nr_letters)]

    password_sy = [random.choice(symbols) for char in range(nr_symbols)]

    password_num = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_lt + password_sy + password_num

    random.shuffle(password_list)

    passwords = ""
    for char in password_list:
        passwords += char

    pass_ent.insert(0, passwords)
    pyperclip.copy(passwords)

# -------------------------------------------------- SAVE PASSWORD -------------------------------------------------- #


def save():
    new_data = {
        web_ent.get(): {
            "Email": email_ent.get(),
            "Password": pass_ent.get(),
        }
    }
    if len(web_ent.get()) == 0 or len(email_ent.get()) == 0 or len(pass_ent.get()) == 0:
        messagebox.showerror(title="Opps", message="Please don't leave any fields")
    else:
        is_ok = messagebox.askokcancel(title=web_ent.get(), message=f"Data entered: \n{email_ent.get()}\n "
                                                                    f"{pass_ent.get()}\n Is it okay to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            web_ent.delete(0, END)
            pass_ent.delete(0, END)


# ------------------------------------------------------ UI SETUP---------------------------------------------------- #

# ---------------------------- WINDOW ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

# ---------------------------- CANVAS ------------------------------- #

canvas = Canvas(height=200, width=190)
photo = PhotoImage(file="logo.png")
canvas.create_image(95, 100, image=photo)
canvas.grid(row=0, column=1)

# ---------------------------- LABELS ------------------------------- #

website = Label(text="Website")
website.grid(row=1, column=0)

email = Label(text="Email")
email.grid(row=2, column=0)

password = Label(text="Password")
password.grid(row=3, column=0)

# ---------------------------- ENTRIES ------------------------------- #

web_ent = Entry()
web_ent.grid(row=1, column=1)
web_ent.focus()

email_ent = Entry()
email_ent.grid(row=2, column=1, columnspan=2)
email_ent.config(width=34)
email_ent.insert(0, "ranarajput1409@gmail.com")

pass_ent = Entry()
pass_ent.grid(row=3, column=1)

# ---------------------------- BUTTONS ------------------------------- #

gnr_pswd = Button(text="Generate Password", command=passwrd)
gnr_pswd.grid(row=3, column=2)


add = Button(text="Add", command=save)
add.grid(row=4, column=1, columnspan=2)
add.config(width=35)

search = Button(text="Search", command=pass_search)
search.config(width=13)
search.grid(row=1, column=2)

window.mainloop()
