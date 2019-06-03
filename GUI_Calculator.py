#1st Import the Tkinter Module

from tkinter import *
from tkinter import ttk
global expression


#Create a frame with variable as Box
box=Tk()

#Provide the Title
box.title("Calculator")

#Adding a Entry with the capacity of 50 characters and making the allign ment
entry=ttk.Entry(box, width=50)
entry.grid(row=0,column=0, columnspan=4)


#Adding the buttons as per the calculator and allignment of the buttons.
def bu_9():
    entry.insert(END,'9')
button_9=ttk.Button(box, text = '9',command=lambda:bu_9())
button_9.grid(row=1,column=0)


def bu_8():
    entry.insert(END,'8')
button_8=ttk.Button(box, text = '8',command=lambda:bu_8())
button_8.grid(row=1,column=1)


def bu_7():
    entry.insert(END,'7')
button_7=ttk.Button(box, text = '7',command=lambda:bu_7())
button_7.grid(row=1,column=2)


def bu_Add():
    entry.insert(END,'+')
button_Add=ttk.Button(box, text = '+',command=lambda:bu_Add())
button_Add.grid(row=1,column=3)


def bu_4():
    entry.insert(END,'4')
button_4=ttk.Button(box, text = '4',command=lambda:bu_4())
button_4.grid(row=2,column=0)


def bu_5():
    entry.insert(END,'5')
button_5=ttk.Button(box, text = '5',command=lambda:bu_5())
button_5.grid(row=2,column=1)


def bu_6():
    entry.insert(END,'6')
button_6=ttk.Button(box, text = '6',command=lambda:bu_6())
button_6.grid(row=2,column=2)


def bu_Sub():
    entry.insert(END,'-')
button_Sub=ttk.Button(box, text = '-',command=lambda:bu_Sub())
button_Sub.grid(row=2,column=3)


def bu_1():
    entry.insert(END,'1')
button_1=ttk.Button(box, text = '1',command=lambda:bu_1())
button_1.grid(row=3,column=0)


def bu_2():
    entry.insert(END,'2')
button_2=ttk.Button(box, text = '2',command=lambda:bu_2())
button_2.grid(row=3,column=1)


def bu_3():
    entry.insert(END,'3')
button_3=ttk.Button(box, text = '3',command=lambda:bu_3())
button_3.grid(row=3,column=2)


def bu_mul():
    entry.insert(END,'*')
button_mul=ttk.Button(box, text = '*',command=lambda:bu_mul())
button_mul.grid(row=3,column=3)


def bu_c():
    entry.delete(0,END)
button_c=ttk.Button(box, text = 'c',command=lambda:bu_c())
button_c.grid(row=4,column=0)


def bu_0():
    entry.insert(END,'0')
button_0=ttk.Button(box, text = '0',command=lambda:bu_0())
button_0.grid(row=4,column=1)


def bu_Eq():
    try:
        total=entry.get()
        entry.delete(0,END)

        total=str(eval(total))
        entry.insert(0, total)
    except:
        entry.insert(0, "Error")
        
            
button_Eq=ttk.Button(box, text = '=',command=lambda:bu_Eq())
button_Eq.grid(row=4,column=2)


def bu_div():
    entry.insert(END,'/')
button_div=ttk.Button(box, text = '/',command=lambda:bu_div())
button_div.grid(row=4,column=3)



box.resizable(0,0)



'''
try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set(" Error ")
        expression=""
'''
