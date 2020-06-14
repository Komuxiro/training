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
    print(response.text)


# define the window's appearance (определим место появления окна)
btn_Weather = Button(root, text='Weather', foreground='black', command=tell_weather)
btn_Weather.bind("<Button-1>", tell_weather)
btn_Weather.grid(row=0, column=1)

date_ent = Frame(root, relief=SUNKEN, bd=4, bg='white')
date_ent.grid()

weather_output = Label(root, text="Нажмите 'Weather' чтобы получить прогноз погоды")
weather_output.grid(row=1, column=1)

# определим оформление календаря
cal = DateEntry(date_ent, dateformat=3, width=12, background='white', foreground='black', borderwidth=4, Calendar=2020)
cal.grid(row=1, column=3, sticky='nsew')

# define the weather (определим погоду)
url = 'http://wttr.in/?0T'
response = requests.get(url)  # выполните HTTP-запрос
print(response.text)  # напечатайте текст HTTP-ответа

root.mainloop()
