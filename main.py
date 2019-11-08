from tkinter.ttk import *
from tkinter import *
import time
import random
from tkinter import messagebox
from PIL import Image, ImageTk

images = []
i = -1
best = 0


def start(finestra):
    j = 20
    for i in range(0, 5):
        load = Image.open("./img/light_off.jpg")
        load = load.resize((80, 150), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(finestra, image=render)
        img.image = render
        images.append(img)

    for img in images:
        img.place(x=j, y=20)
        j += 80
    return j


def restart():
    btn['text'] = "Start"
    btn['command'] = lambda: countdown(finestra)
    for i in images:
        load = Image.open("./img/light_off.jpg")
        load = load.resize((80, 150), Image.ANTIALIAS)
        load = ImageTk.PhotoImage(load)
        i.configure(image=load)
        i.image = load


def off():
    for i in images:
        load = Image.open("./img/light_off.jpg")
        load = load.resize((80, 150), Image.ANTIALIAS)
        load = ImageTk.PhotoImage(load)
        i.configure(image=load)
        i.image = load


def b(finestra, now, wait):
    global best
    restart()
    btn['text'] = "Start"
    btn['command'] = lambda: countdown(finestra)

    tempo = round(((time.time() - now) * 1000) - wait, 3)
    if tempo > 0:
        if tempo < best or best == 0:
            best = tempo
            besttime['text'] = "Miglior tempo di reazione: {}ms".format(best)
        messagebox.showinfo("GG", "Tempo di reazione: {} millisecondi".format(tempo))
    elif tempo <= 0:
        messagebox.showinfo("Fail", "Jump start!")
        restart()


def change(i, finestra):
    load = Image.open("./img/light_on.jpg")
    load = load.resize((80, 150), Image.ANTIALIAS)
    load = ImageTk.PhotoImage(load)
    i.configure(image=load)
    i.image = load
    countdown(finestra)


def countdown(finestra):
    global i
    btn['text'] = "Press me!"
    btn['command'] = lambda: b(finestra, now, wait)

    if i < 4:
        finestra.after(1000, lambda: change(images[i], finestra))
        i += 1
    else:
        i = -1
        wait = random.randint(250, 2000)
        finestra.after(wait, lambda: off())

        now = time.time()


finestra = Tk()
finestra.title("Lights out")
j = start(finestra)
finestra.geometry("{}x250".format(str(j + 20)))

# finestra['background'] = "white"

besttime = Label(finestra, text="Miglior tempo di reazione: {}ms".format(best))
besttime.place(x=20, y=225)
btn = Button(finestra, text="start", command=lambda: countdown(finestra))
btn.place(x=j / 2, y=200)

finestra.mainloop()
