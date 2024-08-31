from tkinter import *

window = Tk()
canvas = Canvas(window, height=500, width=500)

canvas.create_arc(0, 0, 500, 500, fill="teal", extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill="white", extent=180, start=180, width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)
canvas.pack()

window.mainloop()
