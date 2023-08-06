from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.title("my gui")
root.geometry("800x600")

a = Label(text="welcome to my new project", fg="cyan", bg="black", font="algerian 20 bold", padx=20, pady=20)
a.pack(padx=20, pady=10)

def scroll():
   print("adding a scroll bar")

def help():
    print("i will help you")
    tmsg.showinfo("help", "let me help you")

def tip():
    print("giving a tip")
    tmsg.showinfo("tip", "please wear mask and sanitize your hand regularly")

def rate():
    print("rate my gui")
    val = tmsg.askquestion("Experience", "was your experience good ?")
    if val == "yes":
        msg = "please rate us on the app store."
    else:
        msg = "tell us the problem , we will work on it."
    tmsg.showinfo("feedback", msg)
def about():
    tmsg.showinfo("info", '''this is a small project created my abhishek , thanks for using it.''')

mainmenu = Menu(root)

m1 = Menu(mainmenu)
m1.add_command(label="new file")
m1.add_command(label="save")
m1.add_command(label="exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu)
m2.add_command(label="undo")
m2.add_command(label="cut")
m2.add_command(label="copy")
m2.add_command(label="paste")
m2.add_command(label="add scroll", command=scroll)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu)
m3.add_command(label="help", command=help)
m3.add_command(label="tip of the day", command=tip)
m3.add_command(label="rate", command=rate)
m3.add_command(label="about", command=about)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

root.config(background="grey")

Button(text="close", command=root.destroy, font="arial 15 bold", relief=SUNKEN).pack(anchor=S)

root.mainloop()
