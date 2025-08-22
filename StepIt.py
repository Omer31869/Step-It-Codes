from tkinter import *

root = Tk()
root.geometry("450x450")
root.title("MyApp")

students = {
     1: {"name": "Huseyn", "surname": "Ibrahimov", "age": "22"},
     2: {"name": "Omer", "surname": "Nerimanov", "age": "15"},
     3: {"name": "Seid", "surname": "Huseynov", "age": "15"}
}

x = IntVar()
y = IntVar()
z = IntVar()

def check():
    if x.get() == 1:
        s = students[1]
        print(f"1-ci şagird: {"name"} {"surname"}, Yaş: {"age'"}")
    if y.get() == 1:
        s = students[2]
        print(f"2-ci şagird: {s['name']} {s['surname']}, Yaş: {s['age']}")
    if z.get() == 1:
        s = students[3]
        print(f"3-cü şagird: {s['name']} {s['surname']}, Yaş: {s['age']}")

checkB1 = Checkbutton(root, text="Secim 1", variable=x, command=check)
checkB2 = Checkbutton(root, text="Secim 2", variable=y, command=check)
checkB3 = Checkbutton(root, text="Secim 3", variable=z, command=check)

checkB1.pack()
checkB2.pack()
checkB3.pack()

root.mainloop()

