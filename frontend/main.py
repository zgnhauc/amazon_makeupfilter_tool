from tkinter import *


root = Tk()
root.title("Amazon Makeup Filter Tool")
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options1 = [
    "oily",
    "normal",
    "dry"
]
clicked = StringVar()
clicked.set("Select Skin Type")  

drop = OptionMenu(root, clicked, *options1)
drop.pack()

options2 = [
    "<$100", 
    "$100 - $200",
    "$200+"
]
clicked = StringVar()
clicked.set("Select Price Range")

drop = OptionMenu(root, clicked, *options2)
drop.pack()

root.mainloop()
