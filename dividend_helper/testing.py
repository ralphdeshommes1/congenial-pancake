from tkinter import *
import math

def details():
    blank += "this is working"
    




def main():
    window = Tk()
    window.geometry("300x300")
    window.title("dividend optimization")
    entry = Entry(window)
    entry.pack()
    user_input = entry.get()
    frame = Frame(window)
    frame.pack()
    enter_button = Button(frame, text="Enter", command=details)
    enter_button.pack(side=LEFT) 
    blank = Label(window, text="hello")
    blank.pack()

    window.mainloop()



if '__main__' == __name__:
    main()