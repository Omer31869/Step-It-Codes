from tkinter import *

root = Tk()
root.geometry("450x450")
root.title("MyApp")

x = StringVar()

def control():
    print("Seçilən rəng:", x.get())
    root.config(bg=x.get()) 


radioB = Radiobutton(root, text="Option 1", value="green", variable=x, command=control)
radioB.pack()

radioB2 = Radiobutton(root, text="Option 2", value="blue", variable=x, command=control)
radioB2.pack()

radioB3 = Radiobutton(root, text="Option 3", value="red", variable=x, command=control)
radioB3.pack()

root.mainloop()




    
