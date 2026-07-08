#tkinter for gui
import tkinter
from tkinter import *
#
from PIL.ImageTk import *

#multithreading
import threading

#logging
import logger

#read file function
from filereader import read_binary_file

#other
from time import strftime

#c module
import oma

if __name__ == "__main__":
    #simple logger
    logger1 = logger.Logger("Logger 1")

    #graphics window size
    canvasWidth = 800
    canvasHeight = 600


    #read world from file

    #test picture
    picture_file : str = read_binary_file("kuva.bmp")

    #start render thread with world


    # callback function for renderer to send images back


    #################################################################
    #window loops with .mainloop no manual loop needed...
    window : Tk = Tk("WindowTitle")


    #################################################################
    #key event logger for window
    def key_pressed(event):
        if not event.char: logger1.log("KeyPressed event without printable character")

        else:
            logger1.log(f'{event.char} pressed')



    def key_released(event):
        if not event.char:
            logger1.log("KeyReleased event without printable character")
        else:
            logger1.log(f'{event.char} released')

    def mouse_button_pressed(event):
        #<ButtonPress event state=Mod1 num=1 x=12 y=11>
        if not event.char:
            logger1.log("Keypress event without printable character")
        else:
            logger1.log(f'{event} on mouse')

        if event.num == 1:
            logger1.log("Mouse button 1 (left) pressed")
        elif event.num == 2:
            logger1.log("Mouse button 2 (wheel) pressed")
        elif event.num == 3:
            logger1.log("Mouse button 3 (right) pressed")
        elif event.num == 4:
            logger1.log("Mouse button 4 (back) pressed")
        elif event.num == 5:
            logger1.log("Mouse button 5 (forward) pressed")

    def mouse_movement(event):
        if event.char:
            logger1.log(f'Mouse movement on {event}')


    window.bind("<KeyPress>", key_pressed)
    window.bind("<KeyRelease>", key_released)
    window.bind("<Button>", mouse_button_pressed)
    #mouse movement
    window.bind("<Motion>", mouse_movement)

    #################################################################
    # element holding buttons
    button_bar: Widget = tkinter.Frame(window)
    button_bar.pack()


    #some buttons
    close_window_button : Button = Button(button_bar, text = "Close")
    close_window_button.bind("<Button-1>", lambda e: window.destroy())
    close_window_button.grid(column=0, row=0)

    toggle_logger_button : Button = Button(button_bar, text = "Toggle Logger")
    toggle_logger_button.bind("<Button-1>", lambda e: logger1.toggle_logger() )
    toggle_logger_button.grid(column=0, row=1)

    #packing is exclusive with griding
    #toggle_logger_button.pack()
    #close_window_button.pack()

    #################################################################
    #text label clock
    label = Label(button_bar, text = "This should show time")
    label.grid(column=0, row=4)

    #recursive looping function for clock
    def updateLabelFunction():
        label["text"] = strftime("%Y-%m-%d %H:%M:%S")
        label.after(100, updateLabelFunction)

    #run the function
    updateLabelFunction()

    #################################################################
    # label showing results from c module
    label2 = Label(button_bar, text="This should show return value from c function")
    label2.grid(column=0, row=5)

    #function calling c function
    def run_c_function():
        label2["text"] = ""

    #button for running the c function
    run_c_function_button: Button = Button(button_bar, text="Run c function")
    run_c_function_button.bind("<Button-1>", lambda e: run_c_function())
    run_c_function_button.grid(column=0, row=2)




    #################################################################
    #canvas for showing image

    #frame for canvas
    canvas_frame: Frame = Frame(window)
    canvas_frame.pack(side = "bottom", fill = "both", expand = True)

    #pack canvas to frame
    canvas : Widget = tkinter.Canvas(canvas_frame, width=canvasWidth, height=canvasHeight, background="black")
    canvas.pack()

    #test canvas for showing image
    #tällainen: class PIL.ImageTk.PhotoImage(image: Image | str | None = None, size: tuple[int, int] | None = None, **kw: Any)

    photo_image : PhotoImage = PhotoImage(file="kuva.bmp")
    #creating a label without taking return value variable
    Label(canvas_frame, image = photo_image).pack()


    canvas2: Widget = tkinter.Canvas(canvas_frame, width=500, height=500, background="green")
    canvas2.pack()

    #start window loop
    window.mainloop()