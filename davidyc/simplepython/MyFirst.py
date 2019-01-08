from tkinter import *

clicked = 0

def Click():
	global clicked
	clicked += 1
	root.title("Мой первый интерфейс на Python нажатий клавиш {0}".format(clicked))
	
     





root = Tk()
root.title("Мой первый интерфейс на Python нажатий клавиш {0}".format(clicked))
root.geometry("800x250")

btm = Button(text="Click Me", padx="20", pady="8", font="16", command=Click)
			 
			 
			 
			 
btm.pack()
root.mainloop()