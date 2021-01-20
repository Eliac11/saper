from tkinter import *
from tkinter import messagebox

##АЛГОРИТМ ВТОРОЙ


def get(P,test=False):
    
    for x in range(0,len(P)):
        for y in range(0,len(P[0])):
            open = 0
            if P[x][y]["ch"] != "not":
                if P[x][y]["ch"] != 0:


                    for i in range(-1,2):
                        for i2 in range(-1,2):
                            
                            if x+i >= 0 and x+i < len(P):
                                if y+i2 >= 0 and y+i2 < len(P[0]):
                                    if P[x+i][y+i2]["ch"]  == "not":
                                        open += 1
                    try:

                        ch = round(P[x][y]["ch"] / open, 3)

                        for i in range(-1,2):
                            for i2 in range(-1,2):
                            
                                if x+i >= 0 and x+i < len(P):
                                    if y+i2 >= 0 and y+i2 < len(P[0]):

                                        if P[x+i][y+i2]["ch"]  == "not":
                                            P[x+i][y+i2]["bot_mind"] += ch
                    except:
                        print("")
                                            
    
    if not test:

        madepole(P)


    return searching_min(P)

def searching_min(P):
    G = []
    for x in range(0,len(P)):
        line = []
        for y in range(0,len(P[0])):
            if P[x][y]["bot_mind"] == 0:
                ch = 1000
            else:
                ch = P[x][y]["bot_mind"]
            line += [ch]
        G += [line]


    MIN = {}
    for i in range(0,len(G)):
        if min(G[i]) != 1000:
            MIN.update({min(G[i]):[i,G[i].index(min(G[i]))]}) 
            
    m = 20
    for key in MIN:
        if key < m:
            m = key


    try:
        #print(MIN[m])
        n = MIN[m]
        return MIN[m]
    except:
        messagebox.showwarning("Внимание","Первый шаг всегда надо делать самому...") 
        return "not"
    
   


def madepole(P):
    win2 = Tk()
    win2.title("что думает бот")
    win2.geometry("600x600")
    win2["bg"] = "white"

    hhh = []
    for x in range(0,len(P)):
        line = []
        for y in range(0,len(P[0])):
            if P[x][y]["ch"] != "not":
                bg = "green"
            elif P[x][y]["bot_mind"] != 0:
                bg = "yellow"
            else:
                bg = "white"

            l = Label(win2,text = P[x][y]["bot_mind"],bg = bg,height = 2,width = 4)
            l.grid(column = x,row = y)
            line += [l]
        hhh += [line]
