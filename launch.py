from tkinter import *
xy = []
def getxy():
        global xy, entry1 ,entry2,root
        
        
        xy = [entry1.get(),entry2.get()]
        root.destroy()
##спрос
def sizepole():
    global xy, entry1 ,entry2 , root

    root = Tk()
    root.geometry("300x150")
    root.title("Pole")

    l = Label(text="введите размеры поля, 50 на 35 максимум")
    l.grid(row = 0,columnspan = 2)

    l = Label(text="x\ny")
    l.grid(column = 0,row = 1,rowspan = 2)
    
    entry1 = Entry()
    entry1.grid(row = 1,column = 1)

    entry2 = Entry()
    entry2.grid(row = 2,column = 1)

    b = Button(text = "создать",command = getxy)
    b.grid(row = 3,column = 3)

    root.mainloop()
    return xy