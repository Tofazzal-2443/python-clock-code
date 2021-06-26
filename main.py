from tkinter import *

from time import strftime

tusar  = Tk()
tusar .title('T-Clock')

def time():

	string = strftime('%H:%M:%S \n %p')
	lbl.config(text = string)
	#tusar.geometry('350x200')
	lbl.after(1000, time)

lbl = Label(tusar , font = ('calibri', 40, 'bold'),
			background = 'purple',
			foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()
