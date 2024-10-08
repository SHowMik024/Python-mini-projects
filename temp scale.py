from tkinter import *

def submit():
    print("The temp is:" + str(scale.get()) + "degrees C")

window = Tk()
hotImage = PhotoImage(file='fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,
              font=('consolas', 20),
              tickinterval=10,
              resolution=5,
              troughcolor='#69FAFF',
              fg="#FF1C00",
              bg="#111111"
              )

scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()

coldImage = PhotoImage(file='cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()
