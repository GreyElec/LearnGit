import tkinter as tk
from math import *

root = tk.Tk()
root.title("ID:1750849")

label0 = tk.Label(root, text='GUI Calculator Assignment').grid(row=0, column=0)
radian = tk.IntVar()
radian.set(2)
tk.Radiobutton(root, text="angle", variable=radian, value=1).grid(row=0,
                                                                  column=3)
tk.Radiobutton(root, text='radian', variable=radian, value=2).grid(row=0,
                                                                   column=4)
label1 = tk.Label(root, text="Answer =").grid(row=1, column=0, ipadx=0, padx=0,
                                              sticky=tk.W + tk.E + tk.N)
label2 = tk.Label(root, text=' ').grid(row=0, column=2,
                                       sticky=tk.W + tk.E + tk.N)
result = tk.Entry(root)
result.grid(row=1, column=1, columnspan=4, sticky=tk.W + tk.E + tk.N + tk.S)
data = ""

errorMassage = "Error: Unknown Format. Check your input"


def notationAdd(sign):
	global data
	data += sign[0]
	temp = result.get()
	temp += sign[-1]
	result.delete(0, last='end')
	result.insert(0, str(temp))
	return data


def numIN(sign):
	global data
	temp = result.get()
	data += sign
	temp += sign
	result.delete(0, last='end')
	result.insert(0, str(temp))
	return data


def oneClear():
	global data
	temp = result.get()
	if temp == errorMassage:
		allClear()
		data = ""
	else:
		temp = temp[:-1]
		data = data[:-1]
		result.delete(0, last='end')
		result.insert(0, str(temp))
	return data


def allClear():
	result.delete(0, last="end")
	global data
	data = ""
	return data


def trangleFunc(sign):
	global data
	if radian.get() == 1:
		data += sign[0] + "(pi/180)*"
		temp = result.get()
		temp += sign[-1]
		result.delete(0, last='end')
		result.insert(0, str(temp))
	else:
		data = notationAdd(sign)
	return data


def normalCal():
	global data
	try:
		data = str(eval(str(data)))
		result.delete(0, last='end')
		result.insert(0, data)
		return data
	except:
		result.delete(0, last='end')
		result.insert(0, errorMassage)


buttonPow = tk.Button(root, text="pow(x,y)",
                      command=lambda: notationAdd(["**", "^"]), width=15).grid(row=2,
                                                                               column=0,
                                                                               sticky=tk.W + tk.E + tk.N)
buttonCos = tk.Button(root, text="cos",
                      command=lambda: trangleFunc(["cos("]), width=15).grid(row=2,
                                                                            column=1,
                                                                            sticky=tk.W + tk.E + tk.N)
buttonSin = tk.Button(root, text="sin",
                      command=lambda: trangleFunc(["sin("]), width=15).grid(row=2,
                                                                            column=2,
                                                                            sticky=tk.W + tk.E + tk.N)
buttonTan = tk.Button(root, text="tan",
                      command=lambda: trangleFunc(["tan("]), width=15).grid(row=2,
                                                                            column=3,
                                                                            sticky=tk.W + tk.E + tk.N)
buttonfabs = tk.Button(root, text="abs()",
                       command=lambda: notationAdd(["fabs("]), width=15).grid(row=2,
                                                                              column=4,
                                                                              sticky=tk.W + tk.E + tk.N)
buttonSqrt = tk.Button(root, text="√",
                       command=lambda: notationAdd(["sqrt(", "√("]), width=15).grid(row=3,
                                                                                    column=0,
                                                                                    sticky=tk.W + tk.E + tk.N)
buttonLog = tk.Button(root, text="Log10",
                      command=lambda: notationAdd(["log10("]), width=15).grid(row=3,
                                                                              column=1,
                                                                              sticky=tk.W + tk.E + tk.N)
buttonDel = tk.Button(root, text="<-", command=oneClear, width=15).grid(row=3, column=2,
                                                                        sticky=tk.W + tk.E + tk.N)
buttonClr = tk.Button(root, text="Clr", command=allClear, width=15).grid(row=3, column=3,
                                                                         sticky=tk.W + tk.E + tk.N)
buttonDiv = tk.Button(root, text="÷",
                      command=lambda: notationAdd(["/", "÷"]), width=15).grid(row=3,
                                                                              column=4,
                                                                              sticky=tk.W + tk.E + tk.N)
buttonPow10 = tk.Button(root, text="pow(10,y)",
                        command=lambda: notationAdd(["10**", "10^"]), width=15).grid(
	row=4, column=0,
	sticky=tk.W + tk.E + tk.N)
button7 = tk.Button(root, text="7", command=lambda: numIN("7"), width=15).grid(row=4,
                                                                               column=1,
                                                                               sticky=tk.W + tk.E + tk.N)
button8 = tk.Button(root, text="8", command=lambda: numIN("8"), width=15).grid(row=4,
                                                                               column=2,
                                                                               sticky=tk.W + tk.E + tk.N)
button9 = tk.Button(root, text="9", command=lambda: numIN("9"), width=15).grid(row=4,
                                                                               column=3,
                                                                               sticky=tk.W + tk.E + tk.N)
buttonTime = tk.Button(root, text="x",
                       command=lambda: notationAdd(["*", "x"]), width=15).grid(row=4,
                                                                               column=4,
                                                                               sticky=tk.W + tk.E + tk.N)
buttonPi = tk.Button(root, text="π",
                     command=lambda: notationAdd(["pi", "π"]), width=15).grid(row=5,
                                                                              column=0,
                                                                              sticky=tk.W + tk.E + tk.N)
button4 = tk.Button(root, text='4', command=lambda: numIN("4"), width=15).grid(row=5,
                                                                               column=1,
                                                                               sticky=tk.W + tk.E + tk.N)
button5 = tk.Button(root, text='5', command=lambda: numIN('5'), width=15).grid(row=5,
                                                                               column=2,
                                                                               sticky=tk.W + tk.E + tk.N)
button6 = tk.Button(root, text='6', command=lambda: numIN('6'), width=15).grid(row=5,
                                                                               column=3,
                                                                               sticky=tk.W + tk.E + tk.N)
buttonMinus = tk.Button(root, text='-',
                        command=lambda: notationAdd(["-"]), width=15).grid(row=5,
                                                                           column=4,
                                                                           sticky=tk.W + tk.E + tk.N)
buttonFactorial = tk.Button(root, text="n!",
                            command=lambda: notationAdd(["factorial("]), width=19).grid(
	row=6, column=0,
	sticky=tk.W + tk.E + tk.N)
button1 = tk.Button(root, text='1', command=lambda: numIN("1"), width=15).grid(row=6,
                                                                               column=1,
                                                                               sticky=tk.W + tk.E + tk.N)
button2 = tk.Button(root, text='2', command=lambda: numIN('2'), width=15).grid(row=6,
                                                                               column=2,
                                                                               sticky=tk.W + tk.E + tk.N)
button3 = tk.Button(root, text='3', command=lambda: numIN('3'), width=15).grid(row=6,
                                                                               column=3,
                                                                               sticky=tk.W + tk.E + tk.N)
buttonAdd = tk.Button(root, text="+", command=lambda: notationAdd(["+"]), width=15).grid(
	row=6, column=4,
	sticky=tk.W + tk.E + tk.N)
buttonLeft = tk.Button(root, text='(', command=lambda: notationAdd(['(']), width=15).grid(
	row=7, column=0,
	sticky=tk.W + tk.E + tk.N)
buttonRight = tk.Button(root, text=')',
                        command=lambda: notationAdd([")"]), width=15).grid(row=7,
                                                                           column=1,
                                                                           sticky=tk.W + tk.E + tk.N)
button0 = tk.Button(root, text='0', command=lambda: numIN('0'), width=15).grid(row=7,
                                                                               column=2,
                                                                               sticky=tk.W + tk.E + tk.N)
buttonDot = tk.Button(root, text='.', command=lambda: notationAdd(['.']), width=15).grid(
	row=7, column=3,
	sticky=tk.W + tk.E + tk.N)
buttonEqual = tk.Button(root, text='=', command=lambda: normalCal(), width=15).grid(row=7,
                                                                                    column=4,
                                                                                    sticky=tk.W + tk.E + tk.N)
root.mainloop()
