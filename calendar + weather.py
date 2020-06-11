# main window (основное окно)
from tkinter import *

import requests
from tkcalendar import *

# возможно тоже здесь лишнее

window = Tk()
window.geometry('400x250')
window.title('Calendar + weather')


def get_weath():
    req = requests.get('http://wttr.in/?0T')
    print(req.text)


# define the window's appearance (определим место появления окна)
f2 = Frame(window, width=2000, height=2000, relief=SUNKEN, bd=4, bg='white')
f2.grid()
f3 = Label(window, width=40, height=5, relief=SUNKEN, bd=4, bg='white')
f3.grid(row=0, column=1)

# определим оформление календаря
cal = DateEntry(f2, dateformat=3, width=12, background='white', foreground='black', borderwidth=4, Calendar=2020)
cal.grid(row=1, column=3, sticky='nsew')

# define the weather (определим погоду)
url = 'http://wttr.in/?0T'
response = requests.get(url)  # выполните HTTP-запрос
print(response.text)  # напечатайте текст HTTP-ответа

window.mainloop()
