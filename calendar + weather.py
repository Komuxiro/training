# main window (основное окно)

from tkinter import *

root = Tk()
root.title('Calendar + weather')


# in the main branch of the program there will be a main window, an object of type Block and window launch (в
# основной ветке программы будет главное окно, объект типа Block и запуск окна)
class Block(object):
    pass


first_block = Block()


class Block:
    def __init__(self, master):
        self.main_field = Entry(master, width=35)
        self.moving_next = Button(master, text='Next')
        self.moving_previous = Button(master, text='Previous')
        self.marker = Label(master, bg='black', fg='white', width=30)
        self.main_field.pack()
        self.moving_previous.pack() and self.moving_next.pack()
        self.marker.pack()


root.mainloop()
