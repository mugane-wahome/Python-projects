from tkinter import *

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, END)
            entry.insert(END, result)
        except Exception as e:
            entry.delete(0, END)
            entry.insert(END, "Error")
    elif text == "C":
        entry.delete(0, END)
    else:
        entry.insert(END, text)

root = Tk()
root.geometry("400x500")
root.title("Calculator")

entry = Entry(root, font="Arial 20")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, pady=10, padx=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for button_text in buttons:
    button = Button(root, text=button_text, font="Arial 15")
    button.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
