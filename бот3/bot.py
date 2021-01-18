from tkinter import *
from tkinter import messagebox

##АЛГОРИТМ три


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
                        ch = P[x][y]["ch"] / open

                        for i in range(-1,2):
                            for i2 in range(-1,2):
                            
                                if x+i >= 0 and x+i < len(P):
                                    if y+i2 >= 0 and y+i2 < len(P[0]):

                                        if P[x+i][y+i2]["ch"]  == "not":
                                            if P[x+i][y+i2]["bot_mind"] == 0:
                                                P[x+i][y+i2]["bot_mind"] = ch
                                            else:
                                                P[x+i][y+i2]["bot_mind"] = (P[x+i][y+i2]["bot_mind"] + ch) / 2
                    except:
                        print("")
                                            
    
    if not test:

        madepole(P)


    return searching_min(P)

def searching_min(P):
    
    MIN = {}
    for x in range(0,len(P)):
        for y in range(0,len(P[0])):

            if P[x][y]["bot_mind"] != 0 and P[x][y]["ch"] == "not":
                MIN.update({P[x][y]["bot_mind"]:[x,y]})
                m = P[x][y]["bot_mind"]

    for key in MIN:
        if key < m:
            m = key

    try:
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

            l = Label(win2,text = round(P[x][y]["bot_mind"],3),bg = bg,height = 2,width = 4)
            l.grid(column = x,row = y)
            line += [l]
        hhh += [line]
