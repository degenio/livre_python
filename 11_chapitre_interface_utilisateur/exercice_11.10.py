from tkinter import *


def resize(ev=None):
    label.config(font='Helvetica {} bold'.format(scale.get()))


root = Tk()
root.geometry('350x150')
label = Label(root, text='Texte changeant!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)
scale = Scale(root, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=X, expand=1)
quitter = Button(root, text='Quitter', command=root.quit)
quitter.pack()
root.mainloop()
