from tkinter import *
from fw import *
import random

window = Tk()
V = 9
window.title("Floyd Warshall Algorithim")

window.geometry('1500x700')

greeting = Label(window, text="Hello, welcome to our demo.")
greeting.grid(column=0, row=0)
greeting2 = Label(window, text="Click here for our topological set-up:")
greeting2.grid(column=0, row=1)

def setup():
    init_graph()
    #print out the initial set-up here

setupBtn = Button(window, text="Set-up", command=setup)
setupBtn.grid(column=1, row=1)

def randClicked():
    rn1 = random.randint(0,(V-1))
    rn2 = random.randint(0,(V-1))
    convert = ['A','B','C','D','E','F','G','H','I']
    find_path(convert[rn1], convert[rn2])
    #find random path here


def enterClicked():
    convert = ['A','B','C','D','E','F','G','H','I']
    enterLbl = Label(window, text="Starting node:")
    enterLbl.grid(column=0, row=3)
    node1 = Entry(window,width=10)
    node1.grid(column=1, row=4)
    lbl2 = Label(window, text="Ending node:")
    lbl2.grid(column=0, row=5)
    node2 = Entry(window, width=10)
    node2.grid(column=1, row=6)
    def calc():
        print(node1.get())
        print(node2.get())
        find_path(node1.get(), node2.get())
        #show path
    calcBtn = Button(window, text="Show Path", command=calc)
    calcBtn.grid(column=0,row=7)

    #find user-defined path here

instruction = Label(window, text="Click random if you want to find path between random nodes, else click enter:")
instruction.grid(column=0, row=2)
randBtn = Button(window, text="Random", command=randClicked)
randBtn.grid(column=1,row=2)
enterBtn = Button(window, text="Enter", command=enterClicked)
enterBtn.grid(column=2, row=2)


window.mainloop()
