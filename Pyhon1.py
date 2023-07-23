from tkinter import *
root= Tk()
def Click():
    root.mainloop()
A= Label(root, text=input.get())
A.pack()
input= Entry(A, Text="name")
input.pack()
submit= Button(A,Text="Submit",command=Click)