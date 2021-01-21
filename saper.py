from tkinter import *
import random
import sys
sys.path.insert(0, "bots")
import bot5 as bot


#import neirobot

#import mydeogram
import makedata

#import pygame 
#pygame.init()

from tkinter import messagebox
import saved
import time

import launch
pobet = 0
over = 0
bomb_pri_pob = []

#размеры поля по дифолду
C = 10
R = 10

##спрашиваю размеры
xy = launch.sizepole()

## создание окна
win = Tk()
win.title("сапер")
win.geometry("600x600+300+300")
win["bg"] = "white"




##чтобы букв небыло

try:

    C = int(xy[0])
    R = int(xy[1])
except:
    messagebox.showwarning("Внимание","ну да, создай сам поле '{}' на '{}',\nпосмотрю на тебя".format(xy[0],xy[1]))
    
del xy






##чтобы не было больше или меньше
if C > 60:
    C = 60
elif C == 0:
    C = 1

if R > 35:
    R = 35
elif R == 0:
    R = 1



gogame = True
POLE = []

##победил 
def it_is_win():
    global gogame,pobet,bomb_pri_pob, t
    pobet += 1
    gogame = False

    win["bg"] = "green"
   
    b = 0
    ##открытие всех бомб
    for x in range(0,len(POLE)):
        for y in range(0,len(POLE[0])):
            if POLE[x][y].bomb:
                b += 1
                POLE[x][y].opentext()
                win.update_idletasks()
                
    bomb_pri_pob += [b]

    #if t == False:
        
        #pygame.mixer.music.load('mu\win.mp3')
        #pygame.mixer.music.play()
        
        

##проиграл
def gameover():

    #врем добавил
    #bothod()
    
    #

    global gogame,over
    over += 1
    gogame = False

    for x in range(0,len(POLE)):
        for y in range(0,len(POLE[0])):
            if POLE[x][y].bomb:
                POLE[x][y].opentext()
                win.update_idletasks()
    win["bg"] = "red"

    
    
    
## проверка все ли открыто ?
def vse_open():
    clos = 0
    for x in range(0,len(POLE)):
        for y in range(0,len(POLE[0])):
            POLE[x][y].pixel["bd"] = 2
            if not POLE[x][y].bomb and POLE[x][y].pixel["bg"] == "grey":
                clos += 1
    if clos == 0:
        it_is_win()
        win.update_idletasks()


##класс квадрат 
class kvad(object):
    ##создание квадрата
    def __init__(self,x,y,w,l,bomb = False,bombs_range=0):

        self.pixel = Button(text="",bg = "grey",height = w,width = l,font=("Verdana", 10, "bold"),command =lambda x=x,y=y:clic(x,y))
        self.pixel.grid(column = x+1,row = y+1,padx = 0,pady = 0)

        self.bomb = bomb
        self.bombs_range = bombs_range
    ##открыть квадрат
    def opentext(self):
        if self.bomb == False:
            self.pixel["bg"] = "white"
            if self.bombs_range != 0:
                if self.bombs_range == 1:
                    self.pixel["fg"] = "blue"
                if self.bombs_range == 2:
                    self.pixel["fg"] = "green"
                if self.bombs_range == 3:
                    self.pixel["fg"] = "red"
                if self.bombs_range == 4:
                    self.pixel["fg"] = "purple4"
                if self.bombs_range > 4:
                    self.pixel["fg"] = "Olivedrab4"
                self.pixel["text"] = self.bombs_range
        else:
            self.pixel["bg"] = "red"
    ##обнулене пиксиля
    def res(self):
        self.bomb = False
        self.pixel["text"] = ""
        self.pixel["bg"] = "grey"
        self.pixel["bd"] = 2
        self.bombs_range = 0

#####тут конец класса 

##открыте нужных блоков
def openpix(x,y):
    if POLE[x][y].pixel["bg"] == "grey" and POLE[x][y].bomb == False:
        POLE[x][y].opentext()
        for ix in range(-1,2):
            for iy in range(-1,2):
                if x+ix >= 0 and x+ix < len(POLE) and y+iy >= 0 and y+iy < len(POLE[0]):
                    if POLE[x+ix][y+iy].pixel["bg"] == "grey":
                        if POLE[x+ix][y+iy].bombs_range == 0:
                            if ix == 0 or iy == 0:
                                openpix(x+ix,y+iy)
                                #win.update_idletasks()
                                
                        else:
                            POLE[x+ix][y+iy].opentext()
    
##обработка нажатий
def clic(x,y):
    global gogame
    
    #просто убираю выделение бота
    for x22 in range(0,len(POLE)):
        for y22 in range(0,len(POLE[0])):
            if POLE[x22][y22].pixel["bd"] == 5:
                POLE[x22][y22].pixel["bd"] = 2
                #win.update_idletasks()
                
    #------
    
    if POLE[x][y].bomb and gogame:
        POLE[x][y].opentext()
        gameover()
    elif POLE[x][y].pixel["text"] == "" and gogame:
        openpix(x,y)
        vse_open()
##спам бомб
def spambomb():
    global info
    kolb = 0
    for x in range(0,len(POLE)):
        for y in range(0,len(POLE[0])):
            if random.randint(1,5) == 1:
                POLE[x][y].bomb = True
                kolb += 1
                #POLE[x][y].pixel["bg"] = "red"
    info.config(text = "Мин {} \n это: {} %".format(kolb, round(kolb / (len(POLE)*len(POLE[0])) * 100, 2)))


##растановка  чисел
def spamchisl():
    for x in range(0,len(POLE)):
        for y in range(0,len(POLE[0])):
            if not POLE[x][y].bomb:
                bombs = 0
                for i in range(-1,2):
                    for i2 in range(-1,2):
  
                        if x+i >= 0 and x+i < len(POLE):
                            if y+i2 >= 0 and y+i2 < len(POLE[0]):
                                if POLE[x+i][y+i2].bomb:
                                    bombs += 1
                                    #win.update_idletasks()
                POLE[x][y].bombs_range = bombs




##РЕСТАРТ
def restart():
    #pygame.mixer.music.stop()
    global gogame

    win["bg"] = "white"
    for x in range(0,len(POLE)):
        for y in range(0,len(POLE[0])):
            POLE[x][y].res()
            win.update_idletasks()
            #win.update()
            
    spambomb()
    spamchisl()
    #win.update_idletasks()

    

    gogame = True
    
##преобразование для бота
def botget():
    
    P = []
    for x in range(0,len(POLE)):
        line = []
        for y in range(0,len(POLE[0])):
            if POLE[x][y].pixel["bg"] == "white":
                znach = POLE[x][y].bombs_range
            else:
                znach = "not"
            line += [{"ch":znach,"bot_mind":0}]
        P += [line]
    
    return P

##отправка боту и выделение его ответа
def bothod(test = False):
    global gogame
    if gogame:
        rehenie = bot.get(botget(),test)
        if rehenie != "not" and rehenie != "xz":
            #messagebox.showwarning("Внимание","Он может ошибаться")
            x,y = rehenie
            
            if not test:
                POLE[x][y].pixel["bd"] = 5
                #win.update_idletasks()

            if test:
                clic(x,y)
                return True
        elif rehenie == "xz":
            if not t:
                messagebox.showerror("капец","честно хз(((")

            savg()
            return False
            
            
##сохронение
def savg():
    if gogame:

        saved.savegame(POLE)
    else:
        messagebox.showwarning("Внимание","вы же выйграли,\n ну или...")

##открытие сохранения если оно есть
def open_savg():
    global POLE , gogame
    ##проверка есть ли оно
    if saved.save_is():
        win["bg"] = "white"
        gogame = True
        #удаление старого поля
        for x in range(0,len(POLE)):
            for y in range(0,len(POLE[0])):
                POLE[x][y].pixel.destroy()
        #----
        P = saved.opensav()
        POLE = []
        for x in range(0,len(P)):
            line =[]
            for y in range(0,len(P[0])):
                p = kvad(x,y,1,2,P[x][y]["bomb"],0)
                line += [p]
            POLE +=[line]

        spamchisl()

        #открываю нужные поля и считаю бомбы
        kolb = 0
        for x in range(0,len(P)):
            for y in range(0,len(P[0])):
                if P[x][y]["open"]:
                    POLE[x][y].opentext()
                if POLE[x][y].bomb:
                    kolb += 1
        info.config(text = "Мин {} \n это: {} %".format(kolb, round(kolb / (len(POLE)*len(POLE[0])) * 100, 2)))
    else:
        ##если не нашлось
        messagebox.showwarning("Внимание","Сохронение не нашлось(")



t = False
def test():
    global gogame , pobet , over, bomb_pri_pob, t
    pobet = 0
    over = 0
    bomb_pri_pob = []
    if not t:
        t = True
        testov = 500
        hod = 0
        igr = 0
        runhod = 0
        errorstart = 0

        data_x=[]
        data_y=[]

        for i in range(0,testov):
            
            while True:
                x,y = random.randint(0,len(POLE)-1),random.randint(0,len(POLE[0])-1)
                if POLE[x][y].bomb == False:
                    clic(x,y)
                    break


            

            while gogame and t:
                runhod = hod
                f = bothod(True)
                #win.update()
                #если некуда больше ходить
                if not f:
                    while True:
                        x,y = random.randint(0,len(POLE)-1),random.randint(0,len(POLE[0])-1)
                        if POLE[x][y].bomb == False:
                            clic(x,y)
                            break
                #makedata.selectdata(POLE)
                #win.update()
                #if input() == "c":
                    #makedata.savetofile()


                
                #win.update()
                hod += 1
            
            if runhod == hod:
                errorstart += 1
                print("вам смешно")

            igr += 1
            prots = round(pobet/igr*100,4)
            if i % 10 == 0:
                print(i,"ok",pobet,prots)

                data_x += [igr]
                data_y += [prots]

            restart()

        print("побед: {x} \nпоражений: {y} \nпроцент побед: {z} %".format(x=pobet,y=over,z=pobet/testov*100))
        print("всего ходов: {}  {} %".format(hod, 100 - (over / hod * 100) ))
        print("ошибок при рандоме", errorstart)
        print("бомб при победах",*bomb_pri_pob)
        #makedata.savetofile()
        #mydeogram.statis(data_x,data_y)

        bomb_pri_pob = []

        t = False



obnov = Button(text = "Отчистить поле",command =lambda:restart())
obnov.grid(column = 0,row = 0)

info = Label(text = "0",bg = "white")
info.grid(column = 1,row = 0,columnspan = 3)

bot_saper = Button(text = "получить\nподсказку\nот бота",command = bothod)
bot_saper.grid(column = 0,row = 1,rowspan = 3)

sav = Button(text = "сохранить",command = savg)
sav.place(x=190,y=2)

open_saved = Button(text = "загрузить последнее сохранение",command = open_savg)
open_saved.place(x=270,y=2)

start_test = Button(text = "начать тест бота",command = test)
start_test.grid(column = 0,row = 4)

i = Label(text = "Posti Entertaiment \n Posti Arts",font="Chiller 15",bg = "white")
i.grid(column = 101,row = 101)

##первое создание поля
for x in range(0,C):
    line =[]
    for y in range(0,R):
        p = kvad(x,y,1,2)
        line += [p]
        
    POLE +=[line]
####

##первый
#спам бомб 
spambomb()

#чисел
spamchisl()

## запуск окна
win.update_idletasks()
win.mainloop()

# эхх прощай tk
