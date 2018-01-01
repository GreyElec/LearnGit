import tkinter as tk

root = tk.Tk()
def callback(event):
	print('point at:',event.x,event.y)
frame = tk.Frame(root,width = 200, height = 200)
frame.bind('<Button-1>',callback)
frame.pack()
root.mainloop()