import tkinter

def function():
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    frame.pack()

    Text = tkinter.Text(root,height=8, width = 100)
    Text.pack()
    Text.insert(tkinter.END,"Welcome to Luke Parkin's First calculator. \nPlease use the format: (a & b) & (c & d) \nWhere ABCD are any positive numbers, and & is an operator (+/*-)\nNote that operators do not have to be the same\nfor any abcd you may use n^e where n is abc or d, and e is any positive number.\n\nCurrently only two brackets are supported with BIDMAS, \nHowever more brackets may be used without this.")
    Text.configure(state="disabled")

    root.mainloop()