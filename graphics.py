from tkinter import *

window = Tk()

window.title("Floyd Warshall Algorithim")

window.geometry('1500x700')

greeting = Label(window, text="Hello, welcome to our demo.")
greeting.grid(column=0, row=0)
greeting2 = Label(window, text="Click here for our topological set-up:")
greeting2.grid(column=0, row=1)

def setup():
    print("set-up")
    #print out the initial set-up here

setupBtn = Button(window, text="Set-up", command=setup)
setupBtn.grid(column=1, row=1)

def randClicked():
    print("random")
    #find random path here

def enterClicked():
    enterLbl = Label(window, text="Please enter two nodes:")
    enterLbl.grid(column=0, row=3)
    txt = Entry(window, width=10)
    txt.grid(column=1, row=3)
    #find user-defined path here
    
instruction = Label(window, text="Click random if you want to find path between random nodes, else click enter:")
instruction.grid(column=0, row=2)
randBtn = Button(window, text="Random", command=randClicked)
randBtn.grid(column=1,row=2)
enterBtn = Button(window, text="Enter", command=enterClicked)
enterBtn.grid(column=2, row=2)


window.mainloop()
