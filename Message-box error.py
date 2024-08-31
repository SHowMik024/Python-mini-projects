from tkinter import *
from tkinter import messagebox


def click():
    answer = messagebox.askyesnocancel(title='Yes no cancel',
                                       message='Do u like to get high?',
                                       icon='error')
    if (answer==True):
        print("Your a pothead:)")
    elif (answer==False):
        print("Why u wasting time?")
    else:
        print("Dodging eh?")


window = Tk()
button = Button(window,command=click,text='mash me')
button.pack()
window.mainloop()
