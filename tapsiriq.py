from tkinter import *

def TakeText():
    Text = entry.get()
    label.config(text=f"Sizin Textiniz: {Text}", bg="Orange", fg="Blue")

window = Tk()
window.geometry("1000x1000")
window.title("About Me")

entry = Entry(window, bg="Orange", fg="Blue", font=("Arial", 25))
entry.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.1)

label = Label(window, bg="Orange", fg="Blue")
label.pack()

button = Button(window, text="Texti Cap Et", bg="Orange", fg="Blue", command=TakeText)
button.pack()

window.mainloop()
