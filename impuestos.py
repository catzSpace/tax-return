from tkinter import *

win = Tk()
win.title("impuestos")
win.geometry("400x400")


#primer dato
t1 = Label(win, text="ingrese su edad")
t1.place(x=10, y=10)
e1 = Entry()
e1.place(x=10, y=30)


#segundo dato
t2 = Label(win, text="escribe tus ingresos mensuales en dolares")
t2.place(x=10, y=60)
e2 = Entry()
e2.place(x=10, y=80)


T = Label(win, text="procesando...")
T.pack()
T.place(x=10, y=160)


def cal():
    edad = int(e1.get())
    sueldo = float(e2.get()) #es float ya que los dolares se pueden representar de esta manera

    if edad >= 18 and sueldo >= 250:
        T["text"] = "debes declarar renta"

    else:
        T["text"] = "no debes declarar renta"


b = Button(text="calcular", command=lambda:cal())
b.pack(padx=50, pady=120)



win.mainloop()