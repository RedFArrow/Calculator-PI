import tkinter

def function():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    frame.pack()

    Text = tkinter.Text(root,height=5, width = 30)
    Text.pack()
    Text.insert(tkinter.END,"Helpful information \n about a thing")
    Text.configure(state="disabled")

    root.mainloop()