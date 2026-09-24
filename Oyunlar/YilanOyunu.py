daimport turtle
import time
import random

# Ekran ayarları
ekran = turtle.Screen()
ekran.title("Yılan Oyunu")
ekran.setup(width=600, height=600)
ekran.bgcolor("black")
ekran.tracer(0)  # Animasyonu kapat

# Yılan başı
yonlar = ["up", "down", "right", "left"]
yon = random.choice(yonlar)
bas = turtle.Turtle()
bas.speed(0)
bas.shape("square")
bas.color("white")
bas.penup()
bas.goto(0, 0)
bas.direction = yon

# Yem
yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("red")
yem.penup()
yem.goto(0, 100)

# Kuyruk
kuyruklar = []

# Skor
skor = 0

# Hareket fonksiyonları
def yukari():
    if bas.direction != "down":
        bas.direction = "up"

def asagi():
    if bas.direction != "up":
        bas.direction = "down"

def saga():
    if bas.direction != "left":
        bas.direction = "right"

def sola():
    if bas.direction != "right":
        bas.direction = "left"

def hareket():
    if bas.direction == "up":
        y = bas.ycor()
        bas.sety(y + 20)
    if bas.direction == "down":
        y = bas.ycor()
        bas.sety(y - 20)
    if bas.direction == "right":
        x = bas.xcor()
        bas.setx(x + 20)
    if bas.direction == "left":
        x = bas.xcor()
        bas.setx(x - 20)

# Tuş bağlamaları
ekran.listen()
ekran.onkeypress(yukari, "w")
ekran.onkeypress(asagi, "s")
ekran.onkeypress(saga, "d")
ekran.onkeypress(sola, "a")

# Ana oyun döngüsü
while True:
    ekran.update()

    # Sınır kontrolü
    if bas.xcor() > 290 or bas.xcor() < -290 or bas.ycor() > 290 or bas.ycor() < -290:
        time.sleep(1)
        bas.goto(0, 0)
        bas.direction = random.choice(yonlar)
        skor = 0

    # Yem yendiğinde
    if bas.distance(yem) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        yem.goto(x, y)

        skor += 1

        # Yılanı uzat
        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("square")
        kuyruk.color("gray")
        kuyruk.penup()
        kuyruklar.append(kuyruk)

    # Kuyruğu takip et
    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = bas.xcor()
        y = bas.ycor()
        kuyruklar[0].goto(x, y)

    hareket()

    # Çarpışma kontrolü
    for segment in kuyruklar:
        if segment.distance(bas) < 20:
            time.sleep(1)
            bas.goto(0, 0)
            bas.direction = random.choice(yonlar)
            skor = 0
            for segment in kuyruklar:
                segment.goto(1000, 1000)
            kuyruklar.clear()

    time.sleep(0.1)

ekran.mainloop()
