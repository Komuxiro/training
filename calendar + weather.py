# main window (основное окно)
from tkcalendar import *
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('400x250')
window.title('Calendar + weather')

# скорее всего эту функцию можно будет убрать
def clicked():
    messagebox.showinfo('Погода', 'weather')

# define the window's appearance (определим место появления окна)
f2=Frame(window,width=2000,height=2000,relief=SUNKEN,bd=4,bg='white')
f2.grid()
f3=Frame(window,width=280,height=100,relief=SUNKEN,bd=4,bg='white')
f3.grid(row=0, column=1)
# определим оформление календаря
cal=DateEntry(f2,dateformat=3,width=12, background='darkblue',foreground='white', borderwidth=4,Calendar =2020)
cal.grid(row=1,column=3,sticky='nsew')

# define the weather (определим погоду)

window.mainloop()
