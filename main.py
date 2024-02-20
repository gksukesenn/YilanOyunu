import turtle
import time     # Time belli yerlerde belli bir süre beklemek için oluşturuldu.
import random   # Randomu ise yemin random olması için import ettik.
import playsound

Liste = []
skor = 0
maxSkor = 0

# Çerçeve ayarları
w = turtle.Screen()  # Çerçeve ayarlamak için w nesnesi oluşturuyoruz.
w.title("Yılan Oyunu")
w.setup(600, 600)  # boyut
w.bgcolor("green")  # arka plan rengi
w.tracer(0)  # Ekran güncelleme ayarını 0 ile kapattık.

# Yılanın kafa kısmı
yn = turtle.Turtle()
yn.speed(0)
yn.shape("circle")
yn.color("black")
yn.penup()
yn.goto(0, 0)
yn.yon = "dur"

# Yem nesnesi

yem = turtle.Turtle()
yem.speed(0)
yem.shape("circle")
yem.color("brown")
yem.penup()
yem.goto(0, 100)


def hareket():
    if yn.yon == "ust":
        y = yn.ycor()   # y ekseninde yukarı git
        yn.sety(y+20)
    if yn.yon == "alt":
        y = yn.ycor()   # y ekseninde aşağı git
        yn.sety(y-20)
    if yn.yon == "sag":
        x = yn.xcor()   # x ekseninde sağa git
        yn.setx(x+20)
    if yn.yon == "sol":
        x = yn.xcor()   # x ekseninde sola git
        yn.setx(x-20)


def yukarigit():
    if yn.yon != "alt":
        yn.yon = "ust"


def asagigit():
    if yn.yon != "ust":
        yn.yon = "alt"


def sagagit():
    if yn.yon != "sol":
        yn.yon = "sag"


def solagit():
    if yn.yon != "sag":
        yn.yon = "sol"


w.listen()
w.onkeypress(yukarigit, "Up")
w.onkeypress(asagigit, "Down")
w.onkeypress(sagagit, "Right")
w.onkeypress(solagit, "Left")


def ye():
    if yn.distance(yem) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        yem.goto(x, y)

        kuyruk = turtle.Turtle()
        kuyruk.speed(0)
        kuyruk.shape("circle")
        kuyruk.color("white")
        kuyruk.penup()
        Liste.append(kuyruk)

        global skor
        global maxSkor
        skor += 5
        if skor > maxSkor:
            maxSkor = skor
            w.title("Skor:{} En yüksek skor: {}" .format(skor, maxSkor))

    uzunluk = len(Liste)
    for indis in range(uzunluk-1, 0, -1):
        x = Liste[indis-1].xcor()
        y = Liste[indis - 1].ycor()
        Liste[indis].goto(x, y)
    if len(Liste) > 0:
        x = yn.xcor()
        y = yn.ycor()
        Liste[0].goto(x, y)


def baslangic():
    global skor
    time.sleep(0.1)
    yn.goto(0, 0)
    yn.yon = "dur"

    for kuyruk_parca in Liste:
        kuyruk_parca.goto(1000, 1000)
    Liste.clear()
    skor = 0

    w.title("Skor:{} En yüksek puan: {}".format(skor, maxSkor))


while True:
    w.update()
    ye()
    hareket()
    if yn.xcor() > 290 or yn.xcor() < -290 or yn.ycor() > 290 or yn.ycor() < -290:
        playsound.playsound("false.mp3")
        baslangic()
    for eklem in Liste:
        if eklem.distance(yn) < 20:
            playsound.playsound("false.mp3")
            baslangic()
    time.sleep(0.1)
