from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_box.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_input.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        email = data[website]["email"]
        password = data[website]["password"]

        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {email}\n"
                                                       f"Password: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_to_file():
    website = website_input.get()
    email = email_input.get()
    password = password_box.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field", message="You have left a field blank.")

    else:

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_box.delete(0, END)
            email_input.insert(0, "@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Password Manager")
w.minsize(width=200, height=200)
w.config(padx=35, pady=35)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry()
website_input.config(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

search_website_button = Button(text="Search", command=search_website)
search_website_button.config(width=14)
search_website_button.grid(column=2, row=1)

email_label = Label()
email_label.config(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry()
email_input.config(width=35)
email_input.insert(0, "@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label()
password_label.config(text="Password:")
password_label.grid(column=0, row=3)

password_box = Entry()
password_box.config(width=21)
password_box.grid(column=1, row=3)

generate_password_button = Button(text="Generate password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add password", command=save_to_file)
add_button.config(width=36)
add_button.grid(column=1, row=4, columnspan=2)

w.mainloop()