from tkinter import *
from tkinter.tix import ButtonBox

# import tkinter as Tk

root = Tk()

root['bg'] = '#fafafa' 

root.title('Название проги')

root.wm_attributes('-alpha', -0.7)

frame = Frame(root)
frame.place(relx= 0.15, rely= 0.15, relwidth= 0.7, relheight= 0.7)

title = Label(frame, text= 'Somsing text', bg='gray', font= 40)
title.pack()

button = Button(frame, text= 'button', bg='green')
button.pack()

root.geometry('500x350')

root.mainloop()

