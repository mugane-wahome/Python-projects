from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        pass

def clear_tasks():
    tasks_listbox.delete(0, END)

root = Tk()
root.title("To-Do List")

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat")

task_entry = ttk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = ttk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

clear_button = ttk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=5)

tasks_listbox = Listbox(root, width=50)
tasks_listbox.pack(padx=10, pady=10)

root.mainloop()
