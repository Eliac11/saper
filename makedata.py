import pickle 

DATA = []

def selectdata(P):
    global DATA
    data = []

    for x in range(0,len(P)):
        for y in range(0,len(P[0])):
            
            if P[x][y].pixel["bg"] == "white" and P[x][y].bombs_range != 0:

                for x2 in range(-1,2):
                    for y2 in range(-1,2):

                        if x+x2 >= 0 and x+x2 < len(P):
                            if y+y2 >= 0 and y+y2 < len(P[0]):

                                if P[x+x2][y+y2].pixel["bg"] == "grey":
                                     
                                    re = makesee(P,x+x2,y+y2)

                                    if not re is DATA:
                                        DATA += [re]
def makesee(P,x,y):
    d = [0,[]]

    if P[x][y].bomb:
        d[0] = 1

    for x2 in range(-5,5):
        for y2 in range(-5,5):

            if x2 != 0 or y2 != 0:

                try:
                    if P[x+x2][y+y2].pixel["bg"] == "grey":
                        d[1] += [-1]
                    else:
                        d[1] += [P[x+x2][y+y2].bombs_range]
                except:
                    d[1] += [-2]
    return d

def savetofile():
    global DATA

    with open("nerodata.txt","wb") as f:

        pickle.dump(DATA,f)

    print("vse")