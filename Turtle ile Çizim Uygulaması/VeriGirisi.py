from turtle import*
N=int(numinput("poligon","kenar sayısı",5))
renk=textinput("renk","iç rengi")

pensize(4)


begin_fill()
fillcolor(renk)
circle(100,360,N)
end_fill()
