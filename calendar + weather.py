# main window (основное окно)
from tkinter import *

import requests
from tkcalendar import *

root = Tk()
root.geometry('400x250')
root.title('Calendar + weather')


def tell_weather():
    url = 'http://wttr.in/?0T'
    response = requests.get(url)
    x = response.json()


# define the window's appearance (определим место появления окна)
f1 = Button(root,text='Weather', foreground='black')
f1.grid(row=0, column=1)
f2 = Frame(root, relief=SUNKEN, bd=4, bg='white')
f2.grid()
f3 = Label(root, width=40, height=5, relief=SUNKEN, bd=4, bg='white')
f3.grid(row=1, column=1)

# определим оформление календаря
cal = DateEntry(f2, dateformat=3, width=12, background='white', foreground='black', borderwidth=4, Calendar=2020)
cal.grid(row=1, column=3, sticky='nsew')

# define the weather (определим погоду)
url = 'http://wttr.in/?0T'
response = requests.get(url)  # выполните HTTP-запрос
print(response.text)  # напечатайте текст HTTP-ответа

root.mainloop()
