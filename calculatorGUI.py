from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("220x400")
root.title("Calculator by Vineet")
root.wm_iconbitmap("calculator.ico")
root.configure(background="yellow")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold",bg="black",fg="white")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f=Frame(root,bg="black")
b=Button(f,text="C",padx=16,pady=5,font="lucida 16 bold",bg="grey",fg="red")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="%",padx=10,pady=5,font="lucida 16 bold",bg="grey",fg="green")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="/",padx=15,pady=5,font="lucida 16 bold",bg="grey",fg="green")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="7",padx=6,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="8",padx=5.5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="9",padx=5.5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="*",padx=5.5,pady=5,font="lucida 16 bold",bg="grey",fg="green")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="4",padx=6.5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="5",padx=6.3,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="6",padx=6.3,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="-",padx=5.9,pady=5,font="lucida 16 bold",bg="grey",fg="green")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="1",padx=5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="2",padx=5.5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="3",padx=5.5,pady=10,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="+",padx=5.5,pady=5,font="lucida 16 bold",bg="grey",fg="green")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f.pack()



f=Frame(root,bg="black")
b=Button(f,text="00",padx=5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="0",padx=5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text=".",padx=5,pady=5,font="lucida 16 bold",bg="grey",fg="white")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)

b=Button(f,text="=",padx=5,pady=5,font="lucida 16 bold",bg="green",fg="black")
b.pack(side=LEFT,padx=5,pady=5)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()