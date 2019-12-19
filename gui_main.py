import tkinter
import gui_help
import parsingengine
##https://www.python-course.eu/tkinter_dialogs.php

def function():
    global entry1
    string = entry1.get()
    result = (parsingengine.parsingengine(string))
    Text.configure(state="normal")
    Text.delete(1.0,tkinter.END)
    Text.insert(1.0,result)
    Text.configure(state="disabled")

def helpmenu():
    gui_help.function()

root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack()

entry1 = tkinter.Entry(root, bd = 5)
entry1.pack(side=tkinter.TOP)
entry1.focus_set()

button = tkinter.Button(frame,text="CALCULATE",fg="blue",command= function)
button.pack(side=tkinter.LEFT)

button = tkinter.Button(frame,text="HELP",fg="red",command=helpmenu)
button.pack(side=tkinter.BOTTOM)


Text = tkinter.Text(root,height=1, width = 30
                    
                    )

Text.pack()
Text.insert(tkinter.END,'')
Text.configure(state="disabled")



root.mainloop()
