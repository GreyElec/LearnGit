import tkinter as tk
def call():
	return var.set('motherfucker')
root = tk.Tk()
root.title('hello?')
var = tk.StringVar()
var.set('hi?')
frame = tk.Frame(root)
frame.pack()
lable1 = tk.Label(frame,textvariable = var)
lable1.pack()
button1 = tk.Button(frame,text = 'try me',command = call)
button1.pack()
root.mainloop()