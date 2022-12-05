from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

PriceList = {'Капучино': 73, 'Латте': 78, 'Раф': 82, 'Американо': 73,
             'Сахар': 3, '1': 3, '2': 6, '3': 9, '4': 12}
res = None
res2 = None
a = None
b = None
result = None

NewValues = []


class Window:

    def create_window(self, name, size, welcome):
        window.title(name)
        window.geometry(size)
        window.resizable(False, False)
        lbl = Label(window, text=welcome, font=("Arial", 20))
        lbl.pack()

    def messagebox(self):
        btn = Button(window, text='Выбрать', command=clicked)
        btn.pack()

    def Combobox(self, name1, name2, name3, name4, type, text):
        lbl = Label(window, text=text, font=("Times New Roman", 16))
        lbl.pack()
        combo['values'] = (name1, name2, name3, name4)
        # combo.current(0)
        global a
        global NewValues
        global res
        combo.pack()

    def Combobox2(self, name1, name2, name3, name4, type, text):
        lbl = Label(window, text=text, font=("Times New Roman", 16))
        lbl.pack()
        combo2['values'] = (name1, name2, name3, name4)
        # combo.current(0)
        global b
        global NewValues
        global res2
        combo2.pack()
        # a = combo.get()
        # res = NewValues.append(PriceList.get(a))


class Window_menu:

    def create_window_menu(self):
        window_2.title("МЕНЮ")
        window_2.geometry("300x300+1000+100")
        window_2.resizable(False, False)
        lbl = Label(window_2,
                    text="КОФЕ\n\nКапучино - 73 руб. \n Латте - 78 руб. \n Раф - 82 руб. \n Американо - 73 руб. "
                         "\n\n САХАР \n\n 1 кубик - 3 руб. \n\n",
                    font=("Times New Roman", 12))
        lbl.pack()


def clicked():
    global a
    global result
    global NewValues
    global res
    global res2
    global b
    a = combo.get()
    b = combo2.get()
    res = NewValues.append(PriceList.get(a))
    res2 = NewValues.append(PriceList.get(b))
    for i in PriceList:
        if i == a:
            res = PriceList.get(i)
        if i == b:
            res2 = PriceList.get(i)
    result = res + res2
    messagebox.showinfo('Стоимость вашего заказа', result)


window = Tk()
window_2 = Tk()
combo = Combobox(window)
combo2 = Combobox(window)
new_window = Window()
window_menu = Window_menu()

new_window.create_window("Покупка кофе", "600x600+400+100",
                         "Добро пожаловать в кофейню Станислава")
new_window.Combobox("Капучино", "Раф", "Латте", "Американо",
                    "кофе", "Выберите кофе")
new_window.Combobox2(1, 2, 3, 4, "сахар", "Сколько сахара добавить?")

new_window.messagebox()

window_menu.create_window_menu()

window.mainloop()

