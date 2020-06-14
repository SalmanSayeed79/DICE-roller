import random
from tkinter import *
from PIL import Image, ImageTk
#made a change just to watch what happens

def number():
    a=random.randint(1,6)
    print(a)
    #name='{}.ico'.format(a)
#file=Image.open(name)
    #file=file.resize((60,60))
    #files=ImageTk.PhotoImage(file)

    #print(files)
    label2=Label(frame1,text=a,bg='#C2F77B',font='Cambria')

    label2.pack()
root=Tk()
root.geometry('500x500')
root.configure(background="#F9E79F")
root.title("Dice Roller")
root.iconbitmap('main.ico')
#a=Image.open('10.png')

#image1=ImageTk.PhotoImage(Image.open('1.ico'))
#sign=Label(root,image=image1)
#sign.pack()
#files=ImageTk.PhotoImage(Image.open('10.png'))

frame1=LabelFrame(root,height=300,width=300,bg='#C2F77B',padx=50)

frame1.pack(expand='Yes',side=TOP)

Label1=Label(frame1,text="click the button to roll the dice:",bg='#C2F77B',font="Cambria")
Label1.pack()

button1=Button(frame1,bg='red',activebackground='blue',padx=50,command=number)
button1.pack()


root.mainloop()
