import tkinter

m = tkinter.Tk()
w = tkinter.Button(m, text='Stop', width=25, command=m.destroy )
w.pack()
m.mainloop()
