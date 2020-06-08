# main window (основное окно)

from tkinter import *

root = Tk()
root.title('Calendar + weather')

b1 = Button(text='Previous').grid(row=0, column=1)
b2 = Button(text='Next').grid(row=0, column=2)

# days of the week
d1 = Label(text='ПН').grid(row=1, column=1)
d2 = Label(text='ВТ').grid(row=1, column=2)
d3 = Label(text='СР').grid(row=1, column=3)
d4 = Label(text='ЧТ').grid(row=1, column=4)
d5 = Label(text='ПТ').grid(row=1, column=5)
d6 = Label(text='СБ').grid(row=1, column=6)
d7 = Label(text='ВС').grid(row=1, column=7)

# numbers
n1 = Button(text='1 ').grid(row=2, column=1)
n2 = Button(text='2 ').grid(row=2, column=2)
n3 = Button(text='3 ').grid(row=2, column=3)
n4 = Button(text='4 ').grid(row=2, column=4)
n5 = Button(text='5 ').grid(row=2, column=5)
n6 = Button(text='6 ').grid(row=2, column=6)
n7 = Button(text='7 ').grid(row=2, column=7)
n8 = Button(text='8 ').grid(row=3, column=1)
n9 = Button(text='9 ').grid(row=3, column=2)
n10 = Button(text='10').grid(row=3, column=3)
n11 = Button(text='11').grid(row=3, column=4)
n12 = Button(text='12').grid(row=3, column=5)
n13 = Button(text='13').grid(row=3, column=6)
n14 = Button(text='14').grid(row=3, column=7)
n15 = Button(text='15').grid(row=4, column=1)
n16 = Button(text='16').grid(row=4, column=2)
n17 = Button(text='17').grid(row=4, column=3)
n18 = Button(text='18').grid(row=4, column=4)
n19 = Button(text='19').grid(row=4, column=5)
n20 = Button(text='20').grid(row=4, column=6)
n21 = Button(text='21').grid(row=4, column=7)
n22 = Button(text='22').grid(row=5, column=1)
n23 = Button(text='23').grid(row=5, column=2)
n24 = Button(text='24').grid(row=5, column=3)
n25 = Button(text='25').grid(row=5, column=4)
n26 = Button(text='26').grid(row=5, column=5)
n27 = Button(text='27').grid(row=5, column=6)
n28 = Button(text='28').grid(row=5, column=7)
n29 = Button(text='29').grid(row=6, column=1)
n30 = Button(text='30').grid(row=6, column=2)
n31 = Button(text='31').grid(row=6, column=3)

# place position
'''
b1.pack(side=TOP)
b2.pack(side=TOP)

d1.pack(side=LEFT)
d2.pack(side=LEFT)
d3.pack(side=LEFT)
d4.pack(side=LEFT)
d5.pack(side=LEFT)
d6.pack(side=LEFT)
d7.pack(side=LEFT)
'''
'''
n1.pack(side=LEFT)
n2.pack(side=LEFT)
n3.pack(side=LEFT)
n4.pack(side=LEFT)
n5.pack(side=LEFT)
n6.pack(side=LEFT)
n7.pack(side=LEFT)

n8.pack(side=LEFT)
n9.pack(side=LEFT)
n10.pack(side=LEFT)
n11.pack(side=LEFT)
n12.pack(side=LEFT)
n13.pack(side=LEFT)
n14.pack(side=LEFT)
n15.pack(side=LEFT)
n16.pack(side=LEFT)
n17.pack(side=LEFT)
n18.pack(side=LEFT)
n19.pack(side=LEFT)
n20.pack(side=LEFT)
n21.pack(side=LEFT)
n22.pack(side=LEFT)
n23.pack(side=LEFT)
n24.pack(side=LEFT)
n25.pack(side=LEFT)
n26.pack(side=LEFT)
n27.pack(side=LEFT)
n28.pack(side=LEFT)
n29.pack(side=LEFT)
n30.pack(side=LEFT)
n31.pack(side=LEFT)
'''
'''
# in the main branch of the program there will be a main window, an object of type Block and window launch (в
# основной ветке программы будет главное окно, объект типа Block и запуск окна)
class Block(object):
    pass


first_block = Block()


class Block:
    def __init__(self, master):
        self.main_field = Entry(master, width=35)
        self.moving_next = b1(master, text='Next')
        self.moving_previous = b2(master, text='Previous')
        self.marker = Label(master, bg='black', fg='white', width=30)
        self.main_field.pack()
        self.moving_previous.pack() and self.moving_next.pack()
        self.marker.pack()
'''

root.mainloop()
