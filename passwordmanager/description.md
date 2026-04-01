# START OF CODE
Tkinter is a crossplatform GUI toolkit, that allows creation of windows, buttons, text boxes, and more using Python.
```python
from tkinter import *
from tkinter import messagebox #module of code, not a class
from random import choice, randint, shuffle
import pyperclip #clips message
import json

FONT = "Felix Titling", 8

```
# PASSWORD GENERATOR

```pyton
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=f"{password}")
    pyperclip.copy(password)#puts generated password on yourclipboard

```

## SAVE PASSWORD & SEARCH INFO

```python
def search():
        website = website_entry.get()
        try:
            with open("input_file.json") as password_dictionary:
                data = json.load(password_dictionary)#load in dictionary format

        except FileNotFoundError:
            messagebox.showinfo(title="Error",
                                message=f"No Data File Found")
        else:
            #for items in data:
            if website in data:
                messagebox.showinfo(title=f"{website}", message=f"Email:{data[website]['email']} \nPassword:{data[website]['password']}")

            else:
                messagebox.showinfo(title=f"Error",
                                    message=f"No details for {website} exists.")


def save():
    website = website_entry.get()
    uname_or_mail = uname_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": uname_or_mail,
            "password": password
        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message= "Please don't leave any fields empty!")

    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail/username: {mail}\nPassword: {password}\nIs is okay to save?")

        # if is_ok:
        try:
            with open("input_file.json", "r") as pass_manager:#"input_file.txt", "a"appends
                #pass_manager.write(f"{website} | {mail} | {password}\n")
                data = json.load(pass_manager)#converts to python dictionary for display, "r" read

        except FileNotFoundError:
            with open("input_file.json", "w") as pass_manager:
                json.dump(new_data, pass_manager, indent= 4)#saving updated data.. indent easier to read

        else:
            data.update(new_data)#updates data with new data

            with open("input_file.json", "w") as pass_manager:
                data = json.load(pass_manager)
                json.dump(data, pass_manager, indent=4)

#read and update then write..
        finally:
            website_entry.delete(0, END)
            uname_entry.delete(0, END)
            password_entry.delete(0, END)#removes first character 0, to end or last character

```
# UI SETUP

```python
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=228)
bg_img = PhotoImage(file="logo2.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row= 0)#visibility, packs items on screen
#columnspan

#label
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)
uname_label = Label(text="Email/Username:", font=FONT)
uname_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

#input
website_entry = Entry(width= 32)
website_entry.grid(column=1, row= 1)
website_entry.focus()#puts cursor in fields
uname_entry = Entry(width= 32)
uname_entry.grid(column=1, row= 2)
uname_entry.insert(0, string="username")
password_entry = Entry(width= 32)
password_entry.grid(column=1, row= 3)

#buttons
search_btn = Button(text="Search", width=15, font=FONT, command=search)
search_btn.grid(column=2, row=1)
pass_gen_btn = Button(text="Generate Password", font=FONT, command=generate_pass)
pass_gen_btn.grid(column=2, row= 3)
add_btn = Button(text="Add", width= 40, font=FONT, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


screen.mainloop()#screen remains active
``` 
