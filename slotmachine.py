import turtle
from turtle import *
from random import *
import time
import math
from math import *
import os
import sys

screensize(350, 300)
bgcolor('black')

tracer(False)
Design1 = Turtle()
Design1.hideturtle()



#DRAWING DETAILS
#Drawing board
Design1.penup()
Design1.goto(-115, -70)
Design1.pendown()
Design1.color('gold')
Design1.pensize(3.2)
for i in range(2):
    Design1.fd(220)
    Design1.circle(17,90)
    Design1.fd(90)
    Design1.circle(17,90)

Design1.penup()
Design1.color('silver')
Design1.pensize(0.8)
Design1.goto(-48,40)
Design1.rt(90)
Design1.pendown()
Design1.fd(100)

Design1.penup()
Design1.goto(43,40)
Design1.pendown()
Design1.fd(100)

#Writing text
Design1.penup()
Design1.goto(0,240)
Design1.color('white')
Design1.write('Dobrodošli u digitalni jednoruki jack,\nu prozor za ulogu novca morate upisati\nbroj kuna koji želite uložiti u automat kako\nbi ga pokrenuli. Statistika se nalazi ovdje\nispod teksta.', move=False, align='center', font=('arial', 10, 'normal'))

#Drawing statistics
xSta=-280
for i in range(5):
    Design1.goto(xSta,180)
    Design1.shape('square')
    Design1.shapesize(3.5)
    Design1.color('white')
    Design1.stamp()
    Design1.shapesize(3.4)
    Design1.color('black')
    Design1.stamp()
    xSta=xSta+130


Design1.goto(-280, 150)
Design1.color('yellow')
Design1.write('🍋',move=False, align='center', font=('Arial', 44,' normal'))

Design1.goto(-150, 150)
Design1.color('red')
Design1.write('🍉',move=False, align='center', font=('Arial', 44,' normal'))

Design1.goto(-20, 150)
Design1.color('lightgreen')
Design1.write('💶',move=False, align='center', font=('Arial', 44,' normal'))

Design1.goto(110, 150)
Design1.color('green')
Design1.write('🍀',move=False, align='center', font=('Arial', 44, 'normal'))

Design1.goto(240, 150)
Design1.color('silver')
Design1.write('🩸',move=False, align='center', font=('Impact', 44, 'normal'))


Design1.color('white')
Design1.goto(-243, 160)#-37
Design1.write('×2',move=False, align='left', font=('Arial', 27, 'bold'))

Design1.goto(-113, 160)
Design1.write('×3',move=False, align='left', font=('Arial', 27, 'bold'))

Design1.goto(17, 160)
Design1.write('×4',move=False, align='left', font=('Arial', 27, 'bold'))

Design1.goto(147, 160)
Design1.write('×5',move=False, align='left', font=('Arial', 27, 'bold'))

Design1.goto(277, 160)
Design1.write('×6',move=False, align='left', font=('Arial', 27, 'bold'))


Design1.goto(-250,35)
Design1.write('Uloženo:',move=False, align='center', font=('Arial', 9, 'normal'))
Design1.goto(250,35)
Design1.write('Nagrada:',move=False, align='center', font=('Arial', 9, 'normal'))
#

Thing1 = Turtle()
Thing2 = Turtle()
Thing3 = Turtle()

Thing1.color('silver')
Thing1.penup()
Thing1.goto(-85, -35)
Thing1.hideturtle()

Thing2.color('silver')
Thing2.penup()
Thing2.goto(-2.5, -35)#Važno
Thing2.hideturtle()

Thing3.color('silver')
Thing3.penup()
Thing3.goto(82.5, -35)
Thing3.hideturtle()

#CRTANJE PROGRAMA GOTOVO, AKCIJA PROGRAMA
Uloga1 = numinput('Uloga novaca', 'Koliko želite uložiti kuna u automat(4 znamenke najviše)?', minval=1, maxval=9999)
Uloga1 = round(Uloga1)

while True:

    Design1.goto(-250, 17)
    Design1.write(Uloga1, move=True, align='right', font=('Arial', 12, 'bold'))
    Design1.lt(90)
    Design1.fd(12)
    Design1.write('kn', move=False, align='center', font=('Arial', 12, 'bold'))


    Thing1.write('...', move=False, align='center', font=('Arial', 45, 'normal'))
    Thing2.write('...', move=False, align='center', font=('Arial', 45, 'normal'))
    Thing3.write('...', move=False, align='center', font=('Arial', 45, 'normal'))

    #Varijable za slučajan odabir
    Dobitak1=0
    Dobitak2=0
    Dobitak3=0

    time.sleep(1)

    Dobitak1 = randint(2, 6)
    if Dobitak1==2:
        Thing1.color('black')
        Thing1.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing1.color('yellow')
        Thing1.write('🍋',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak1==3:
        Thing1.color('black')
        Thing1.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing1.color('red')
        Thing1.write('🍉',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak1==4:
        Thing1.color('black')
        Thing1.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing1.color('lightgreen')
        Thing1.write('💶',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak1==5:
        Thing1.color('black')
        Thing1.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing1.color('green')
        Thing1.write('🍀',move=False, align='center', font=('Arial', 44, 'normal'))
    if Dobitak1==6:
        Thing1.color('black')
        Thing1.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing1.color('silver')
        Thing1.write('🩸',move=False, align='center', font=('Impact', 44, 'normal'))


    time.sleep(1)

    Dobitak2 = randint(2, 6)
    if Dobitak2==2:
        Thing2.color('black')
        Thing2.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing2.color('yellow')
        Thing2.write('🍋',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak2==3:
        Thing2.color('black')
        Thing2.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing2.color('red')
        Thing2.write('🍉',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak2==4:
        Thing2.color('black')
        Thing2.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing2.color('lightgreen')
        Thing2.write('💶',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak2==5:
        Thing2.color('black')
        Thing2.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing2.color('green')
        Thing2.write('🍀',move=False, align='center', font=('Arial', 44, 'normal'))
    if Dobitak2==6:
        Thing2.color('black')
        Thing2.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing2.color('silver')
        Thing2.write('🩸',move=False, align='center', font=('Impact', 44, 'normal'))


    time.sleep(1)

    Dobitak3 = randint(2, 6)
    if Dobitak3==2:
        Thing3.color('black')
        Thing3.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing3.color('yellow')
        Thing3.write('🍋',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak3==3:
        Thing3.color('black')
        Thing3.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing3.color('red')
        Thing3.write('🍉',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak3==4:
        Thing3.color('black')
        Thing3.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing3.color('lightgreen')
        Thing3.write('💶',move=False, align='center', font=('Arial', 44,' normal'))
    if Dobitak3==5:
        Thing3.color('black')
        Thing3.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing3.color('green')
        Thing3.write('🍀',move=False, align='center', font=('Arial', 44, 'normal'))
    if Dobitak3==6:
        Thing3.color('black')
        Thing3.write('▇', move=False, align='center', font=('Arial', 66, 'normal'))
        Thing3.color('silver')
        Thing3.write('🩸',move=False, align='center', font=('Impact', 44, 'normal'))


    Design1.goto(250, 13)
    Design1.color('yellow')

    time.sleep(0.5)

    if Dobitak1==Dobitak2==Dobitak3==2:
        Nagrada=Uloga1*2
        Design1.write(Nagrada, move=True, align='right' , font=('Arial', 15, 'bold'))
        Design1.fd(12)
        Design1.write('kn', move=False, align='center', font=('Arial', 15, 'bold'))

    elif Dobitak1==Dobitak2==Dobitak3==3:
        Nagrada=Uloga1*3
        Design1.write(Nagrada, move=True, align='right' , font=('Arial', 15, 'bold'))
        Design1.fd(12)
        Design1.write('kn', move=False, align='center', font=('Arial', 15, 'bold'))

    elif Dobitak1==Dobitak2==Dobitak3==4:
        Nagrada=Uloga1*4
        Design1.write(Nagrada, move=True, align='right' , font=('Arial', 15, 'bold'))
        Design1.fd(12)
        Design1.write('kn', move=False, align='center', font=('Arial', 15, 'bold'))

    elif Dobitak1==Dobitak2==Dobitak3==5:
        Nagrada=Uloga1*5
        Design1.write(Nagrada, move=True, align='right' , font=('Arial', 15, 'bold'))
        Design1.fd(12)
        Design1.write('kn', move=False, align='center', font=('Arial', 15, 'bold'))

    elif Dobitak1==Dobitak2==Dobitak3==6:
        Nagrada=Uloga1*6
        Design1.write(Nagrada, move=True, align='right' , font=('Arial', 15, 'bold'))
        Design1.fd(12)
        Design1.write('kn', move=False, align='center', font=('Arial', 15, 'bold'))

    else:
        Design1.color('red')
        Design1.write('✖', move=False, align='center', font=('Arial', 15, 'bold'))
        Design1.color('silver')
    time.sleep(2)

    Izbor = numinput('Pitanje', 'Dali želite pokušati ponovo?\n1=Da\n2=Ne', minval=1, maxval=2)
    Izbor = round(Izbor)
    if Izbor==1:
        Thing1.color('black')
        Thing1.lt(90)
        Thing1.bk(20)
        Thing1.write('▇', move=False, align='center', font=('Arial', 83, 'normal'))
        Thing1.write('...', move=False, align='center', font=('Arial', 45, 'normal'))
        Thing2.color('black')
        Thing2.lt(90)
        Thing2.bk(20)
        Thing2.write('▇', move=False, align='center', font=('Arial', 83, 'normal'))
        Thing3.color('black')
        Thing3.lt(90)
        Thing3.bk(20)
        Thing3.write('▇', move=False, align='center', font=('Arial', 83, 'normal'))
        Thing1.fd(20)
        Thing2.fd(20)
        Thing3.fd(20)
        Thing1.rt(90)
        Thing2.rt(90)
        Thing3.rt(90)
        continue
    if Izbor==2:
        sys.exit()

    

