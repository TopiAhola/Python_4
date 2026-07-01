#tkinter for gui
import tkinter
from time import strftime
from tkinter import *

#multithreading
import threading





if __name__ == "__main__":
    #graphics window size
    canvasWidth = 800
    canvasHeight = 600


    #read world from file


    #start render thread with world


    # callback function for renderer to send images back


    #################################################################
    #window loops with .mainloop no manual loop needed...
    window : Tk = Tk("WindowTitle")


    #################################################################
    #key event logger for window
    def key_pressed(event):
        if not event.char:
            print("Keypress event without printable character")
        else:
            print(f'{event.char} pressed')

    def key_released(event):
        if not event.char:
            print("KeyReleased event without printable character")
        else:
            print(f'{event.char} released')

    window.bind("<KeyPress>", key_pressed)
    window.bind("<KeyRelease>", key_released)



    #################################################################
    #buttons
    button : Button = Button(window, text = "Close")
    button.bind("<Button-1>", lambda e: window.destroy())
    button.pack()

    #################################################################
    #text label clock
    label = Label(window, text = "This should show time")
    label.pack()

    #recursive looping function for clock
    def updateLabelFunction():
        label["text"] = strftime("%Y-%m-%d %H:%M:%S")
        label.after(100, updateLabelFunction)

    #run the function
    updateLabelFunction()

    #################################################################
    #canvas for showing image

    canvas : Widget = tkinter.Canvas(window, width=canvasWidth, height=canvasHeight, background="black")
    #canvas.setvar("background", "black")

    canvas.pack()

    #start window loop
    window.mainloop()