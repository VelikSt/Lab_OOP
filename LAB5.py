from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Деление с остатком с использованием исключений.")
root.geometry("500x350+500+250")

lbl1 = Label(root, text="Введите числитель:")
lbl1.pack()
e1 = ttk.Entry(root)
e1.pack()

lbl3 = Label(root, text="Введите знаменатель:")
lbl3.pack()
e2 = ttk.Entry(root)
e2.pack()


def clicked():
    m = e1.get()
    m1 = e2.get()
    try:
        s = int(m)
        s1 = int(m1)
        lbl2 = Label(root, text=s / s1)
        lbl2.pack()
    except ZeroDivisionError:
        lbl2 = Label(root, text='На ноль делить нельзя!')
        lbl2.pack()
    except ValueError:
        lbl2 = Label(root, text='Для начала введите 2 числа!')
        lbl2.pack()

butt = Button(root, text='Подтвердить', command=clicked)
butt.pack()

root.mainloop()
