import pickle
##сохранение
def savegame(POLE):
    P = []
    for x in range(0,len(POLE)):
        line = []
        for y in range(0,len(POLE[0])):
            b = POLE[x][y].bomb
            #r = POLE[x][y].bombs_range
            if POLE[x][y].pixel["bg"] == "grey":
                o = False
            else:
                o = True
            line += [{"bomb":b,"open":o}]
        P += [line]
    with open("mu\s.txt","wb") as f:
        pickle.dump(P, f)
    
def save_is():
    # проверка есть ли сохранение 
    try:
        f = open("mu\s.txt","rb")
        f.close()
        return True
    except:
        return False

##открытие 
def opensav():
    with open("mu\s.txt","rb") as f:
        P = pickle.load(f)
    return P
