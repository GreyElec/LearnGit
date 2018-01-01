import tkinter as tk
from math import *

root = tk.Tk()
root.title('specialCal')

#root.geometry('540x540+0+0')
frame1 = tk.Frame(root)
frame1.pack(side = 'right')
global result
entry = tk.Entry(root)
entry.pack(fill = 'x')

'''
this module is for the normal calculation:
including all the normal cal, however 
there are some scientific calculation option are to be build
'''

def normalCal():
	try:
		disp = eval(entry.get())
		entry.delete(0,last = 'end')
		entry.insert(0,str(disp))
	except:
		entry.delete(0,last='end')
		entry.insert(0,'an error occured')

buttonEqual = tk.Button(frame1,text = '=',command = normalCal)
buttonEqual.pack(side = 'left')

'''
this module realized the sqrt and the power function
which returns you the float type result
'''

def sqrtFun():
	temp = entry.get()
	temp += 'sqrt()'
	entry.delete(0,last='end')
	entry.insert(0,str(temp))
buttonSqrt = tk.Button(root,text = '√',command = sqrtFun)
buttonSqrt.pack(side = 'left')

def powerFun():
	temp = entry.get()
	temp = temp + '**'
	entry.delete(0,last='end')
	entry.insert(0,temp)
buttonPow = tk.Button(root,text = '^',command = powerFun)
buttonPow.pack(side = 'left')

def add():
	temp = entry.get()+'+'
	entry.delete(0,last='end')
	entry.insert(0,temp)
buttonAdd = tk.Button(root,text = '+',command = add)
buttonAdd.pack()

def minus():
	temp = entry.get()+'-'
	entry.delete(0,last='end')
	entry.insert(0,temp)
buttonMinus = tk.Button(root,text = '-',command = minus)
buttonMinus.pack()

def divided():
	temp = entry.get()+'/'
	entry.delete(0,last='end')
	entry.insert(0,temp)
buttonDivided = tk.Button(root,text = '/',command = divided)
buttonDivided.pack()

def times():
	temp = entry.get()+ '*'
	entry.delete(0,last='end')
	entry.insert(0,temp)
buttonTime = tk.Button(root,text = '*',command = times)
buttonTime.pack()


def logFun():
	temp = entry.get()
	temp += 'log10()'
	entry.delete(0,last='end')
	entry.insert(0,str(temp))
buttonLog = tk.Button(root,text = 'Log10',command = logFun)
buttonLog.pack(side = 'left')

def allClr():
	entry.delete(0,last= 'end')
buttonClr = tk.Button(root,text = 'AC',command = allClr)
buttonClr.pack(side = 'left')

def delFun():
	entry.delete(len(entry.get())-1,last='end')
buttonDel = tk.Button(root,text = 'Del',command = delFun)
buttonDel.pack()

'''
by the time of the 27/10/2017 
there are still three main functions remains to be build
trangle functions and the transformation of degree and redians.
'''

def Sin():
	temp = 'sin('+entry.get()+')'
	entry.delete(0,last='end')
	entry.insert(0,temp)
	normalCal()
buttonSin = tk.Button(root,text = 'sin',command = Sin)
buttonSin.pack(side = 'right')
def Cos():
	temp = 'cos('+entry.get()+')'
	entry.delete(0,last='end')
	entry.insert(0,temp)
	normalCal()
buttonCos = tk.Button(root,text = 'cos',command = Cos)
buttonCos.pack(side = 'left')
def Tan():
	temp = 'cos('+entry.get()+')'
	entry.delete(0,last='end')
	entry.insert(0,temp)
	normalCal()
buttonTan = tk.Button(root,text = 'tan',command = Tan)
buttonTan.pack(side = 'left')

root.mainloop()

