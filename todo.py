from tkinter import *

pane = Tk()

c1 = Checkbutton(pane, text="Feed dogs")
c1.grid(sticky=W)
c2 = Checkbutton(pane, text="Watch lecture")
c2.grid(sticky=W)
c3 = Checkbutton(pane, text="Read book")
c3.grid(sticky=W)
c4 = Checkbutton(pane, text="Make food")
c4.grid(sticky=W)
c4 = Checkbutton(pane, text="Design map")
c4.grid(sticky=W)
c6 = Checkbutton(pane, text="Gym")
c6.grid(sticky=W)

pane.mainloop()