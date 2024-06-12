from tkinter import *

window = Tk()
window.title("Simple Calculator")
icon_path = "/home/kishor/projects/learning/FDFS-GENAI-Python/icon.ico"
window.iconbitmap(icon_path)

e = Entry(width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def ButtonClick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def ButtonClear():
    e.delete(0,END)


def ButtonAdd():
    global fnum,math
    first_number = e.get()
    math = 1
    e.delete(0,END)
    fnum = int(first_number)

def ButtonSub():
    global fnum,math
    math = 2
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonMul():
    global fnum,math
    math =3
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonDiv():
    global fnum,math
    math = 4
    first_number = e.get()
    e.delete(0,END)
    fnum = int(first_number)

def ButtonEqual():
    second_number = e.get()
    e.delete(0,END)
    snum = int(second_number)

    if math == 1:
        e.insert(0,fnum+snum)

    elif math == 2:
        e.insert(0,fnum-snum)

    elif math == 3:
        e.insert(0,fnum*snum)

    else:
        e.insert(0,fnum/snum)


button1 = Button(text=1,padx=40,pady=20,command=lambda: ButtonClick(1)).grid(row=1,column=0)
button2 = Button(text=2,padx=40,pady=20,command=lambda: ButtonClick(2)).grid(row=1,column=1)
button3 = Button(text=3,padx=40,pady=20,command=lambda: ButtonClick(3)).grid(row=1,column=2)

button4 = Button(text=4,padx=40,pady=20,command=lambda: ButtonClick(4)).grid(row=2,column=0)
button5 = Button(text=5,padx=40,pady=20,command=lambda: ButtonClick(5)).grid(row=2,column=1)
button6 = Button(text=6,padx=40,pady=20,command=lambda: ButtonClick(6)).grid(row=2,column=2)

button7 = Button(text=7,padx=40,pady=20,command=lambda: ButtonClick(7)).grid(row=3,column=0)
button8 = Button(text=8,padx=40,pady=20,command=lambda: ButtonClick(8)).grid(row=3,column=1)
button9 = Button(text=9,padx=40,pady=20,command=lambda: ButtonClick(9)).grid(row=3,column=2)

button0 = Button(text=0,padx=40,pady=20,command=lambda: ButtonClick(0)).grid(row=4,column=0)
buttonclear = Button(text="Clear",padx=77,pady=20,command=ButtonClear).grid(row=4,column=1,columnspan=2)

buttonadd = Button(text="+",padx=38,pady=20,command=ButtonAdd).grid(row=5,column=0)
buttonequal = Button(text="=",padx=87,pady=20,command=ButtonEqual).grid(row=5,column=1,columnspan=2)


buttonsub = Button(text="-",padx=40,pady=20,command=ButtonSub).grid(row=6,column=0)
buttonmul = Button(text="*",padx=40,pady=20,command=ButtonMul).grid(row=6,column=1)
buttondiv = Button(text="/",padx=40,pady=20,command=ButtonDiv).grid(row=6,column=2)

window.mainloop()