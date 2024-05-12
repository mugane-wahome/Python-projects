from tkinter import *
from tkinter import filedialog, messagebox
import os

def new_file():
    text.delete("1.0", END)
    root.title("Untitled - Text Editor")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text.delete("1.0", END)
            text.insert(END, file.read())
        root.title(os.path.basename(file_path) + " - Text Editor")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", END))
        root.title(os.path.basename(file_path) + " - Text Editor")

def about():
    messagebox.showinfo("About", "This is a simple text editor created using Tkinter.")

root = Tk()
root.title("Untitled - Text Editor")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

text = Text(root, wrap="word", undo=True)
text.pack(expand=True, fill="both")

scrollbar = Scrollbar(text)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

root.mainloop()
