from tkinter import *
from tkinter import messagebox
import random
##АЛГОРИТМ 5



def get(PL,test=False):
    global P
    P = PL
    for x in range(0,len(P)):
        for y in range(0,len(P[0])):
            notopen = 0
            if P[x][y]["ch"] != "not":
                if P[x][y]["ch"] != 0:


                    for i in range(-1,2):
                        for i2 in range(-1,2):
                            
                            if x+i >= 0 and x+i < len(P):
                                if y+i2 >= 0 and y+i2 < len(P[0]):
                                    if P[x+i][y+i2]["ch"]  == "not":
                                        notopen += 1
                    try:
                        ch = P[x][y]["ch"] / notopen

                        for i in range(-1,2):
                            for i2 in range(-1,2):
                            
                                if x+i >= 0 and x+i < len(P):
                                    if y+i2 >= 0 and y+i2 < len(P[0]):
                                        

                                            if P[x+i][y+i2]["ch"]  == "not":
                                                if ch != 1:
                                                    if P[x+i][y+i2]["bot_mind"] != 1:

                                                        if P[x+i][y+i2]["bot_mind"] == 0:
                                                            P[x+i][y+i2]["bot_mind"] = ch
                                                        else:
                                                            
                                                            if ch > P[x+i][y+i2]["bot_mind"]:
                                                                P[x+i][y+i2]["bot_mind"] = (P[x+i][y+i2]["bot_mind"]*10 + ch*20) / 30 

                                                            if ch <= P[x+i][y+i2]["bot_mind"]: 
                                                                P[x+i][y+i2]["bot_mind"] = (P[x+i][y+i2]["bot_mind"]*10 + ch*5) / 15

                                                else:
                                                    P[x+i][y+i2]["bot_mind"] = 1
                    except:
                        pass

#дичь

    for x in range(0,len(P)):
        for y in range(0,len(P[0])):

            if P[x][y]["ch"] != "not":
                if P[x][y]["ch"] != 0:

                    kol_close_kvad_rav1 = 0
                    kol_close_kvad = 0
                    for i in range(-1,2):
                        for i2 in range(-1,2):
                                    
                            if x+i >= 0 and x+i < len(P):
                                if y+i2 >= 0 and y+i2 < len(P[0]):

                                    kol_close_kvad += 1
                                    if P[x+i][y+i2]["bot_mind"] == 1:
                                        kol_close_kvad_rav1 += 1

                    if kol_close_kvad_rav1 < kol_close_kvad:
                        if P[x][y]["ch"] == kol_close_kvad_rav1:

                            for i in range(-1,2):
                                for i2 in range(-1,2):
                                            
                                    if x+i >= 0 and x+i < len(P):
                                        if y+i2 >= 0 and y+i2 < len(P[0]):

                                            if P[x+i][y+i2]["bot_mind"] != 1:
                                                P[x+i][y+i2]["bot_mind"] = 0.01

                    elif kol_close_kvad_rav1 > kol_close_kvad:
                        print(x,y,"какая-то ошибка")
                            


                    
                                            
    if not test:

        madepole(P)


    return searching_min(P)

def searching_min(P):
    
    listpoint = []
    for x in range(0,len(P)):
        for y in range(0,len(P[0])):

            if P[x][y]["bot_mind"] != 0 and P[x][y]["ch"] == "not":
                listpoint += [(P[x][y]["bot_mind"],[x,y])]

    MIN = [listpoint[0]]

    for i in listpoint:
        if i[0] < MIN[0][0]:
            MIN = [i]
        elif i[0] == MIN[0][0]:
            MIN += [i]
            

    try:
        n = random.choice(MIN)
        if n[0] != 1:
            return n[1]
            
        else:
            return "xz"
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
            text = ""
            if P[x][y]["ch"] != "not":
                text = P[x][y]["ch"]
                bg = "green"
            elif P[x][y]["bot_mind"] != 0:
                
                bg = "yellow"
                if P[x][y]["bot_mind"] == 1:
                    text ="явно"
                else:
                    text = round(P[x][y]["bot_mind"],3)
            else:
                text = ""
                bg = "white"

            l = Label(win2,text = text,bg = bg,height = 2,width = 4,bd=5)
            l.grid(column = x,row = y)
            line += [l]
        hhh += [line]
