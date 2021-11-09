import tkinter
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    pass_text.delete(0, 'end')
    lett = ""
    symb = ""
    numb = ""
    for letter in range(0, random.randint(1, 8)):
        lett += letters[random.randint(0, len(letters) - 1)]
    # print(lett)

    for number in range(0, random.randint(1, 8)):
        numb += str(numbers[random.randint(0, len(numbers) - 1)])
    # print(numb)

    for symbol in range(0, random.randint(1, 8)):
        symb += str(symbols[random.randint(0, len(symbols) - 1)])
    # print(symb)

    passe = lett + numb + symb
    pass_list = []
    puss = ""
    for pa in passe:
        pass_list.append(pa)


    for pa in pass_list:
        puss += pa
    pass_text.insert(0,puss)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_file():
    if web_text.get() == "":
        messagebox.showinfo(title="Error",message="Please insert the website")
    elif pass_text.get() == "":
        messagebox.showinfo(title="Error", message="Please insert the password")
    elif email_text.get == "":
        messagebox.showinfo(title="Error", message="Please insert the email")
    else:
        is_ok = messagebox.askokcancel(title=web_text.get(), message=f"Details entered: \nEmail: {email_text.get()} Password: {pass_text.get()} \n Is it ok to save?")
    if is_ok:
        with open("pass_management.txt", mode="a") as management:
            management.write(f"{web_text.get()} | {email_text.get()} | {pass_text.get()} \n")
        web_text.delete(0, 'end')
        pass_text.delete(0, 'end')
        messagebox.showinfo(title="Saved",message="Data Saved!")




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

web_label = tkinter.Label(text="Website: ")
web_label.grid(column=0, row=1)
web_text = tkinter.Entry(width=35)
web_text.grid(column=1, row=1, columnspan=2)
web_text.focus()

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_text = tkinter.Entry(width=35)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, "example@mail.com")

pass_label = tkinter.Label(text="Password")
pass_label.grid(column=0, row=3)
pass_text = tkinter.Entry(width=21)
pass_text.grid(column=1, row=3, columnspan=1)
generate_button = tkinter.Button(text="Generate Password", width=16, command=generate)
generate_button.grid(column=2, row=3, columnspan=2)

add_button = tkinter.Button(text="Add", width=36, command=write_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
