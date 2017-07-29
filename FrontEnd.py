from tkinter import *
from database import *  

def whichSelected () :
    print (select.curselection(), len(database))
    return int(select.curselection()[0])

def addEntry () :
    database.append ([itemVar.get(), itemNum.get()])
    setSelect ()

def updateEntry() :
    database[whichSelected()] = [itemVar.get(), itemNum.get()]
    setSelect ()

def deleteEntry() :
    del database[whichSelected()]
    setSelect ()

def loadEntry  () :
    item, itemVar = database[whichSelected()]
    itemVar.set(item)
    itemNum.set(number)

def makeWindow () :
    global itemVar, itemNum, select
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Item").grid(row=0, column=0, sticky=W)
    itemVar = StringVar()
    item = Entry(frame1, textvariable=itemVar)
    item.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Item Number").grid(row=1, column=0, sticky=W)
    itemNum= StringVar()
    number= Entry(frame1, textvariable=itemNum)
    number.grid(row=1, column=1, sticky=W)

    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)

    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    return win

def setSelect () :
    database.sort()
    select.delete(0,END)
    for item,itemNumber in database :
        select.insert (END, item)

win = makeWindow()
setSelect ()
win.mainloop()

