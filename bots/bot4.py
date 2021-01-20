from tkinter import *
from tkinter import messagebox

##АЛГОРИТМ 4



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

                                                



                                        #opens = 0
                                        #for i3 in range(-1,2):
                                         #   for i4 in range(-1,2):
                            #
                             #                   if x+i+i3 >= 0 and x+i+i3 < len(P):
                              #                      if y+i2+i4 >= 0 and y+i2+i4 < len(P[0]):
                               #                         if y+i2+i4 != 0 or x+i+i3 != 0:
                               #
                                                            #if P[x+i+i3][y+i2+i4]["ch"] != "not":
                                                             #   opens += 1
                            #            if opens == 1:
                             #               if P[x+i][y+i2]["bot_mind"] != 1:
                              #                  if P[x+i][y+i2]["bot_mind"] == 0:
                               #                     P[x+i][y+i2]["bot_mind"] = 1
                                    #            else:
                                    #                P[x+i][y+i2]["bot_mind"] = (P[x+i][y+i2]["bot_mind"] + 1) / 2


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
        if m != 1:
            return MIN[m]
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
                text = ""
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

            l = Label(win2,text = text,bg = bg,height = 2,width = 4)
            l.grid(column = x,row = y)
            line += [l]
        hhh += [line]
