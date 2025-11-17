from tkinter import *


root = Tk()
root.title("Amazon Makeup Filter Tool")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "oily",
    "normal",
    "dry"
]
clicked = StringVar()
clicked.set("Select Skin Type")  

drop = OptionMenu(root, clicked, *options)
drop.pack()

root.mainloop()
