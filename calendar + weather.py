# main window (основное окно)

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x250')
window.title('Calendar + weather')

b1 = Button(text='Previous').grid(row=0, column=1)
b2 = Button(text='Next').grid(row=0, column=7)


def clicked():
    messagebox.showinfo('Погода', 'weather')


# days of the week
d1 = Label(text='ПН').grid(row=1, column=1)
d2 = Label(text='ВТ').grid(row=1, column=2)
d3 = Label(text='СР').grid(row=1, column=3)
d4 = Label(text='ЧТ').grid(row=1, column=4)
d5 = Label(text='ПТ').grid(row=1, column=5)
d6 = Label(text='СБ').grid(row=1, column=6)
d7 = Label(text='ВС').grid(row=1, column=7)

# numbers
n1 = Button(text='1 ', command=clicked).grid(row=2, column=1)
n2 = Button(text='2 ', command=clicked).grid(row=2, column=2)
n3 = Button(text='3 ', command=clicked).grid(row=2, column=3)
n4 = Button(text='4 ', command=clicked).grid(row=2, column=4)
n5 = Button(text='5 ', command=clicked).grid(row=2, column=5)
n6 = Button(text='6 ', command=clicked).grid(row=2, column=6)
n7 = Button(text='7 ', command=clicked).grid(row=2, column=7)
n8 = Button(text='8 ', command=clicked).grid(row=3, column=1)
n9 = Button(text='9 ', command=clicked).grid(row=3, column=2)
n10 = Button(text='10', command=clicked).grid(row=3, column=3)
n11 = Button(text='11', command=clicked).grid(row=3, column=4)
n12 = Button(text='12', command=clicked).grid(row=3, column=5)
n13 = Button(text='13', command=clicked).grid(row=3, column=6)
n14 = Button(text='14', command=clicked).grid(row=3, column=7)
n15 = Button(text='15', command=clicked).grid(row=4, column=1)
n16 = Button(text='16', command=clicked).grid(row=4, column=2)
n17 = Button(text='17', command=clicked).grid(row=4, column=3)
n18 = Button(text='18', command=clicked).grid(row=4, column=4)
n19 = Button(text='19', command=clicked).grid(row=4, column=5)
n20 = Button(text='20', command=clicked).grid(row=4, column=6)
n21 = Button(text='21', command=clicked).grid(row=4, column=7)
n22 = Button(text='22', command=clicked).grid(row=5, column=1)
n23 = Button(text='23', command=clicked).grid(row=5, column=2)
n24 = Button(text='24', command=clicked).grid(row=5, column=3)
n25 = Button(text='25', command=clicked).grid(row=5, column=4)
n26 = Button(text='26', command=clicked).grid(row=5, column=5)
n27 = Button(text='27', command=clicked).grid(row=5, column=6)
n28 = Button(text='28', command=clicked).grid(row=5, column=7)
n29 = Button(text='29', command=clicked).grid(row=6, column=1)
n30 = Button(text='30', command=clicked).grid(row=6, column=2)
n31 = Button(text='31', command=clicked).grid(row=6, column=3)

window.mainloop()
