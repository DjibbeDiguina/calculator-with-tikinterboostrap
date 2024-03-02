
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap import Style

root = tb.Window(themename="cyborg")
root.title("DjibbeCalculator")
root.geometry("400x490")


def display(num):
    entry.insert(END, num)

def clearB():
    entry.delete(0, END)

def Delete():
    entry_text = entry.get()
    new_text = entry_text[:-1]  # Remove the last character
    entry.delete(0, 'end')  # Clear the entry widget
    entry.insert(0, new_text)

def answere():
    ans = entry.get()
    answ= eval(ans)
    clearB()
    entry.insert(0, answ)


entry = tb.Entry(root, font=("Arial", 24, "bold"), bootstyle="dark")
entry.grid(row=0, column=0, pady=20, padx=10, columnspan=4, sticky='news')
style = Style()
style.configure('dark.TButton', foreground='white', font=('Arial', 24, 'bold'))
style.configure('warning.TButton', foreground='white', font=('Arial', 24, 'bold'))
style.configure('danger.TButton', foreground='white', font=('Arial', 24, 'bold'))
style.configure('success.TButton', foreground='white', font=('Arial', 24, 'bold'))
b7 = tb.Button(root, text='7', style='dark.TButton', width=3, command=lambda :display('7'))
b7.grid(row=1, column=0, padx=10, pady=10)
b8 = tb.Button(root, text='8', style='dark.TButton', width=3, command=lambda :display('8'))
b8.grid(row=1, column=1,padx=10)
b9 = tb.Button(root, text='9', style='dark.TButton', width=3, command=lambda :display('9'))
b9.grid(row=1, column=2, padx=10)
plus = tb.Button(root, text='+', style='warning.TButton', width=3, command=lambda :display('+'))
plus.grid(row=1, column=3, padx=10)

b4 = tb.Button(root, text='4', style='dark.TButton', width=3, command=lambda :display('4'))
b4.grid(row=2, column=0, padx=10, pady=10)
b5 = tb.Button(root, text='5', style='dark.TButton', width=3, command=lambda :display('5'))
b5.grid(row=2, column=1,padx=10)
b6 = tb.Button(root, text='6', style='dark.TButton', width=3, command=lambda :display('6'))
b6.grid(row=2, column=2, padx=10)
mul = tb.Button(root, text='*', style='warning.TButton', width=3, command=lambda :display('*'))
mul.grid(row=2, column=3, padx=10)

b1 = tb.Button(root, text='1', style='dark.TButton', width=3, command=lambda :display('1'))
b1.grid(row=3, column=0, padx=10, pady=10)
b2 = tb.Button(root, text='2', style='dark.TButton', width=3, command=lambda :display('2'))
b2.grid(row=3, column=1, padx=10)
b3 = tb.Button(root, text='3', style='dark.TButton', width=3, command=lambda :display('3'))
b3.grid(row=3, column=2, padx=10)
sub = tb.Button(root, text='-', style='warning.TButton', width=3, command=lambda :display('-'))
sub.grid(row=3, column=3, padx=10)

b0 = tb.Button(root, text='0', style='dark.TButton', width=3, command=lambda :display('0'))
b0.grid(row=4, column=0, padx=10, pady=10)
point = tb.Button(root, text='.', style='dark.TButton', width=3, command=lambda :display('.'))
point.grid(row=4, column=1, padx=10)
clear = tb.Button(root, text='C', style='danger.TButton', width=3, command=clearB)
clear.grid(row=4, column=2, padx=10)
div = tb.Button(root, text='/', style='warning.TButton', width=3, command=lambda :display('/'))
div.grid(row=4, column=3, padx=10)

delt = tb.Button(root, text='X', style='danger.TButton', width=3, command=Delete)
delt.grid(row=5, column=0, padx=10, pady=10, sticky='news')
egal = tb.Button(root, text='=', style='success.TButton', width=3, command=answere)
egal.grid(row=5, column=1, padx=10, columnspan=4, sticky='new', pady=10)

label = tb.Label(root, text="Make by DiguinaFils")
label.grid(row=6, column=0, padx=10, pady=10, columnspan=4)
root.mainloop()

