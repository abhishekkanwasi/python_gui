from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

root.title("calculator by Ak")
root.geometry("330x425")
root.maxsize(330, 425)
root.minsize(330, 425)
Label(text="CALCULATOR", font=("Courier New", 15, "bold"), fg="cyan", bg="black", padx=5, pady=5).pack(padx=5, pady=5)
root.config()

def mytip():
    print("no tip")
    tmsg.showinfo("tip", "no tip")

def myquery():
    print("my query")
    a = tmsg.askquestion("query", "do you have a query")
    if a == "yes":
        tmsg.showinfo("Fix", "ok we will fix your probem")
    else:
        tmsg.showinfo("Fix", "ok")


mainmenu = Menu(root)
m1 = Menu(mainmenu)
m1.add_command(label="save")
m1.add_command(label="open")
m1.add_command(label="Close", command=quit)


mainmenu.add_cascade(label="file", menu=m1)

m2 = Menu(mainmenu)
m2.add_command(label="tip", command=mytip)
m2.add_command(label="query", command=myquery)

mainmenu.add_cascade(label="Help", menu=m2)
root.config(menu=mainmenu)

m3 = Menu(mainmenu)
m3.add_command(label="rate")
m3.add_command(label="credits")

mainmenu.add_cascade(label="About", menu=m3)
root.config(menu=mainmenu)

def click(event):

    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        print(value)
        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="ds-digital 25 bold", relief=SUNKEN, fg="black", borderwidth=8, bg="grey")
screen.pack(padx=10, pady=5)

f = Frame(root)
b = Button(f, text="0", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="ds-digital 20 bold", relief=RAISED, padx=5, fg="red", bg="grey")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="/", font="ds-digital 20 bold", relief=RAISED, padx=13, fg="red", bg="grey")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="ds-digital 20 bold", relief=RAISED, padx=9, fg="red", bg="grey")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="9", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="ds-digital 20 bold", relief=RAISED, padx=10, fg="red", bg="grey")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="6", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="ds-digital 20 bold", relief=RAISED, padx=6, fg="red", bg="grey")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="3", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="ds-digital 20 bold", relief=RAISED, padx=10)
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)

b = Button(f, text="c", font="ds-digital 20 bold", relief=RAISED, padx=6, fg="red", bg="grey", cursor="X_cursor")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
b = Button(f, text="=", font="ds-digital 20 bold", relief=RAISED, padx=125, fg="red", bg="grey")
b.pack(side=LEFT, padx=10, pady=2)
b.bind("<Button-1>", click)
f.pack()

can = Canvas(root, width=410, height=10, bg="red")

can.create_line(420, 0, 420, 410, fill="red")
can.create_line(0, 0, 100, 200, fill="red")
can.create_line(420, 0, 420, 410, fill="red")
can.pack()
root.mainloop()
