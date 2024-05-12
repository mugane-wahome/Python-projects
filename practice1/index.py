from tkinter import *

root = Tk()
root.geometry("500x600")
root.title("User Profile")

# User Details
name_label = Label(root, text="Name:", font=("Arial", 12))
name_label.place(x=50, y=50)
name_entry = Entry(root, width=30)
name_entry.place(x=150, y=50)

age_label = Label(root, text="Age:", font=("Arial", 12))
age_label.place(x=50, y=100)
age_entry = Entry(root, width=10)
age_entry.place(x=150, y=100)

email_label = Label(root, text="Email:", font=("Arial", 12))
email_label.place(x=50, y=150)
email_entry = Entry(root, width=30)
email_entry.place(x=150, y=150)

# Profile Display
def display_profile():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()

    profile_label.config(text=f"Name: {name}\nAge: {age}\nEmail: {email}")

display_button = Button(root, text="Display Profile", command=display_profile)
display_button.place(x=200, y=200)

profile_label = Label(root, text="", font=("Arial", 12), justify=LEFT)
profile_label.place(x=50, y=250)

root.mainloop()
