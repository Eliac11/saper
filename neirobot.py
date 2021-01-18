from tkinter import *
from tkinter import messagebox
import random
import pickle

##neiro

import tensorflow as tf
import numpy as np
from tensorflow import keras


model = tf.keras.Sequential([keras.layers.Dense(units=99, input_shape=[99]),keras.layers.Dense(units=33),keras.layers.Dense(units=1)])

#model.compile(optimizer='sgd', loss='mean_squared_error')
model.compile(optimizer=tf.keras.optimizers.Adam(0.01),
              loss='mse',      
              metrics=['mae'])

#model.load_weights('my_checkpoint')
#model.predict([n])

def get(P,test=False):

    for x in range(0,len(P)):
        for y in range(0,len(P[0])):

            notopen = 0

            if P[x][y]["ch"] != "not" and P[x][y]["ch"] != 0:

                    for i in range(-1,2):
                        for i2 in range(-1,2):
                            
                            if x+i >= 0 and x+i < len(P):
                                if y+i2 >= 0 and y+i2 < len(P[0]):
                                    if P[x+i][y+i2]["ch"]  == "not":
                                        P[x+i][y+i2]["bot_mind"] = make_resh(makesee(P,x,y))


    if not test:

        madepole(P)


    return searching_min(P)

def makesee(P,x,y):
    d = []

    for x2 in range(-5,5):
        for y2 in range(-5,5):

            if x2 != 0 or y2 != 0:

                try:
                    if P[x+x2][y+y2]["ch"] == "not":
                        d += [-1]
                    else:
                        d += [P[x+x2][y+y2]["ch"]]
                except:
                    d += [-2]
    return d

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
   
def make_resh(d):
    oncafe = model.predict([d])[0][0]
  
    return oncafe

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

def training_on_data():
    with open("nerodata.txt","rb") as f:
        data = pickle.load(f)

    fitdata = []
    pravotv = []
    for i,i2 in data:
        fitdata += [i2]
        pravotv += [i]

    xs = np.array(fitdata, dtype=int)
    ys = np.array(pravotv, dtype=int)

    model.fit(xs, ys, epochs=10)

    model.save_weights('mozg/my_checkpoint')

if __name__ == "__main__":
    training_on_data()
else:
    model.load_weights('mozg/my_checkpoint')