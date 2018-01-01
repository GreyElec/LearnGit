import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
var = tk.StringVar()
var.set('hello world!')

def call():
	var.set("joke me!")

textlabel = tk.Label(root, textvariable=var)
textlabel.pack()
testButton = tk.Button(root, text='hi motherfucker', command=call)
testButton.pack()
testButton2 = tk.Button(root,textvariable = var,command = root.destroy)
testButton2.pack()
root.mainloop()


