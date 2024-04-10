from tkinter import *
root = Tk()
root.title("------Calculater------")
root.geometry("400x600")
root.minsize(400,600)
root.maxsize(400,600)

#functions for performing some task
def click(event):
    global ans_box_var
    try:
     text = event.widget.cget("text")
     if text == "=":
        if ans_box_var.get().isdigit():
            value = int(ans_box_var.get)
        else:
            value = eval(ans_box_var.get())
        ans_box_var.set(value)
        ans_box.update()
     elif text == "C":
        ans_box_var.set("")
        ans_box.update()

     else:
        ans_box_var.set(ans_box_var.get() + text)
        ans_box.update()
    except:
        ans_box_var.set("Error")
        ans_box.update()
#entry and answer box
ans_box_var = StringVar()
ans_box_var.set("")
ans_box = Entry(font='arial 26 bold',background='lightgray',fg='darkblue',borderwidth=4,textvariable=ans_box_var)
ans_box.pack(padx=6,pady=9)

#frames
f1=Frame(root,background='black')
f1.pack(fill=X,pady=2,padx=4)

f2=Frame(root,background='black')
f2.pack(fill=X,pady=2,padx=4)

f3=Frame(root,background='black')
f3.pack(fill=X,pady=2,padx=4)

f4=Frame(root,background='black')
f4.pack(fill=X,pady=2,padx=4)

f5=Frame(root,background='black')
f5.pack(fill=X,pady=2,padx=4)

f6=Frame(root,background='black')
f6.pack(fill=X,pady=2,padx=4)

#first line for frame f1
n_clear = Button(f1,text='C',font='lucida 25 bold',background='orange',fg='white',padx=127,pady=5)
n_clear.pack(side=LEFT,anchor='ne',padx=3)
n_equal = Button(f1,text='=',font='lucida 25 bold',background='lightblue',fg='red',padx=21,pady=5)
n_equal.pack(side=RIGHT,anchor='ne',padx=3)

#first line bind
n_clear.bind('<Button-1>',click)
n_equal.bind('<Button-1>',click)

#second line for frame f2
n9 = Button(f2,text='9',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n9.pack(side=LEFT,anchor='ne',padx=3)
n8 = Button(f2,text='8',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n8.pack(side=LEFT,anchor='ne',padx=3)
n7 = Button(f2,text='7',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n7.pack(side=LEFT,anchor='ne',padx=3)
n_add = Button(f2,text='+',font='lucida 25 bold',background='lightblue',fg='red',padx=16,pady=10)
n_add.pack(side=RIGHT,anchor='ne',padx=3)

#second line bind
n9.bind('<Button-1>',click)
n8.bind('<Button-1>',click)
n7.bind('<Button-1>',click)
n_add.bind('<Button-1>',click)

#third line for frame f3
n6 = Button(f3,text='6',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n6.pack(side=LEFT,anchor='ne',padx=3)
n5 = Button(f3,text='5',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n5.pack(side=LEFT,anchor='ne',padx=3)
n4 = Button(f3,text='4',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n4.pack(side=LEFT,anchor='ne',padx=3)
n_sub = Button(f3,text='-',font='lucida 25 bold',background='lightblue',fg='red',padx=20,pady=10)
n_sub.pack(side=RIGHT,anchor='ne',padx=3)

#third line bind
n6.bind('<Button-1>',click)
n5.bind('<Button-1>',click)
n4.bind('<Button-1>',click)
n_sub.bind('<Button-1>',click)

#fourth line for frame f4
n3 = Button(f4,text='3',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n3.pack(side=LEFT,anchor='ne',padx=3)
n2 = Button(f4,text='2',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n2.pack(side=LEFT,anchor='ne',padx=3)
n1 = Button(f4,text='1',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n1.pack(side=LEFT,anchor='ne',padx=3)
n_mul = Button(f4,text='*',font='lucida 25 bold',background='lightblue',fg='red',padx=19,pady=10)
n_mul.pack(side=RIGHT,anchor='ne',padx=3)

#fourth line bind
n3.bind('<Button-1>',click)
n2.bind('<Button-1>',click)
n1.bind('<Button-1>',click)
n_mul.bind('<Button-1>',click)

#fifth line for f5
n0 = Button(f5,text='0',font='lucida 25 bold',background='orange',fg='white',padx=26,pady=10)
n0.pack(side=LEFT,anchor='ne',padx=3)
n_dot = Button(f5,text='.',font='lucida 25 bold',background='orange',fg='white',padx=30,pady=10)
n_dot.pack(side=LEFT,anchor='ne',padx=3)
n00 = Button(f5,text='00',font='lucida 25 bold',background='orange',fg='white',padx=17,pady=10)
n00.pack(side=LEFT,anchor='ne',padx=3)
n_div = Button(f5,text='/',font='lucida 25 bold',background='lightblue',fg='red',padx=19,pady=10)
n_div.pack(side=RIGHT,anchor='ne',padx=3)

#fifth line bind
n0.bind('<Button-1>',click)
n_dot.bind('<Button-1>',click)
n00.bind('<Button-1>',click)
n_div.bind('<Button-1>',click)

#sixth line for f6
n_exit = Button(f6,text='Exit',font='lucida 25 bold',background='lightblue',fg='red',pady=10,padx=149,command=quit)
n_exit.pack(side=LEFT,anchor='ne',padx=3)

root.configure(bg='black')
root.mainloop()