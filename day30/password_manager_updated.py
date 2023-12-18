from tkinter import * # only imports all Classes
from tkinter import messagebox # messagebox is a module and not a class
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))] # _ is a throwaway variable
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list) # convert all elements in the list to a string
    password_entry.insert(0, password) # insert the password into the password entry
    pyperclip.copy(password) # copy the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    # check if any of the fields are empty        
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    
    else: # only continue if all fields are filled
        try:
            with open("data.json", "r") as file: 
                # Read
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally: 
            website_entry.delete(0, END) # clear the entry from the 0th index to the end
            password_entry.delete(0, END)
            
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get() # get value of website entry typed by user
    try:
        with open("data.json", "r") as file: 
            # Read the JSON file
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data: # check if the website exists in the data
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}") # \n is a new line
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) # tuple is (x, y)
canvas.pack()
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
# columnspan helps to span the widget over multiple columns
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus() # cursor will be in this entry when program starts
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "beatricekay@hotmail.com") # insert text into entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
# add_button() should save the data from the entries to a file and clear the entries after
add_button = Button(text="Add", width=36, command=save) 
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()