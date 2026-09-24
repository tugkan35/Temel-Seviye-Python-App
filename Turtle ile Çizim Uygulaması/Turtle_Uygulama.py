from turtle import *

def kareCizim(mesafe): #kare çizim fonksiyonu
    for a in range (1,5):
        forward(mesafe)
        left(90)

hideturtle()
pensize(2)
x=int(input("kare sayısı gir:"))
x+=1
for a in range(x):
    kareCizim(50*a)
