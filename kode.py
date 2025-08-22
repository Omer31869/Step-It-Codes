# # from tkinter import *
# # from tkinter  import ttk
# # root = Tk()
# # root.geometry("700x700")

# # spinNumber = IntVar()  

# # def fuc1():
# #     x = spinNumber.get() 
# #     print(x)

# # spin = Spinbox(
# #     root,
# #     from_=1,
# #     to=50,
# #     font=("Comic Sans MS", 30),
# #     textvariable=spinNumber, 
# #     command=fuc1
# # )
# # spin.pack()

# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox

# root = Tk()
# root.geometry("450x450")
# root.title("MyApp")

# # def AylarFunc():
# #     ay = combostr.get()
# #     if ay in ["Yanvar", "Fevral", "Dekabr"]:
# #       messagebox.showinfo("Qiş ayi:", ay)
# #     elif ay in ["Mart", "Aprel", "May"]:
# #         messagebox.showinfo("Yaz ayi:", ay)
# #     elif ay in ["Iyun", "Iyul", "August"]:
# #         messagebox.showinfo("Yay ayi:", ay)
# #     elif ay in ["Sentyabr", "Oktyabr", "Noyabr"]:
# #         messagebox.showinfo("Payiz ayi:", ay)

# # Aylar = ["Yanvar", "Fevral", "Mart", "Aprel", "May",
# #          "Iyun", "Iyul", "August", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"]

# # combostr = StringVar()
# # comboBox = ttk.Combobox(root, values=Aylar, textvariable=combostr, state="readonly")
# # comboBox.pack()

# # button = Button(root, text="Ayi yoxla", command=AylarFunc)
# # button.pack()

# # index = 0 
# # def back():
# #     global index
# #     if index > 0 and index <= len(allFrames) - 1:
# #         allFrames[index].forget()
# #         index -= 1
# #         allFrames[index].pack()
# #     else:
# #         allFrames[index].forget()
# #         index = 0
# #         allFrames[index].pack()

# # def Forward():
# #     global index
# #     if index > 0 and index <= len(allFrames) - 1:
# #         allFrames[index].forget()
# #         index += 1
# #         allFrames[index].pack()
# #     else:
# #         allFrames[index].forget()
# #         index = 0
# #         allFrames[index].pack()

# # frame1 = Frame(root, bg="red", width="300", height="500")
# # frame2 = Frame(root, bg="green", width="300", height="500")
# # frame3 = Frame(root, bg="blue", width="300", height="500")
# # frame4 = Frame(root, bg="yellow", width="300", height="500")
# # frame5 = Frame(root, bg="black", width="300", height="500")
 
# # button = Button(root, text="BACK", command=back)
# # button.pack(side=LEFT)

# # button = Button(root, text="NEXT", command=Forward)
# # button.pack(side=RIGHT)

# # allFrames =[frame1,frame2,frame3,frame4,frame5]
# # root.mainloop()


# def login():
#     LoginFrame = Frame(root, bg="#7A7878" )
#     LoginFrame.pack()
#     def back():
#         LoginFrame.forget()

#         btn= Button(LoginFrame, text="Back", bg="#9C0909", command=back)
#         btn.place(relx= 0.05, rely=0.05, relwidth=0.1, relheight=0.05)

# def signUp():
#     signUpFrame = Frame(root, bg="#9C0909")
#     signUpFrame.pack()

#     def back():
#         signUpFrame.forget()

#     btn= Button(signUpFrame, text="BACK", bg="White", command=lambda:back())
#     btn.place(relx= 0.05, rely=0.05, relwidth=0.1, relheight=0.05)
# root.config(bg="deepskyblue")

# btnLogin = Button(root, text="Login", font=("Arial", 25), command=login)
# root.mainloop()