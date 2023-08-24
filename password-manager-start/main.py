from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list = [choice(letters) for _ in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(message="Oops! Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Read Old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data_file.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Update Old Data with New Data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Save Updated Data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo Image
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

web_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entries
web_input = Entry(width=35)
email_input = Entry(width=35)
password_input = Entry(width=21)

web_input.grid(column=1, row=1, columnspan=2)
email_input.grid(column=1, row=2, columnspan=2)
password_input.grid(column=1, row=3)

web_input.focus()
email_input.insert(0, "joshtipon921@gmail.com")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save)

generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
