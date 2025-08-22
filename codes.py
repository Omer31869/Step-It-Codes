from tkinter import *

root = Tk()
root.geometry("600x400")
root.config(bg="deepskyblue")

def login():
    LoginFrame = Frame(root, bg="#7A7878")
    LoginFrame.place(relx=0, rely=0, relwidth=1, relheight=1)  

    def back():
        LoginFrame.place_forget()  

    btn = Button(LoginFrame, text="Back", bg="#9C0909", fg="white", command=back)
    btn.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)


def signUp():
    signUpFrame = Frame(root, bg="#9C0909")
    signUpFrame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def back():
        signUpFrame.place_forget()

    btn = Button(signUpFrame, text="BACK", bg="White", command=back)
    btn.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)


btnLogin = Button(root, text="Login", font=("Arial", 25), command=login)
btnLogin.place(relx=0.3, rely=0.3)

btnSignUp = Button(root, text="Sign Up", font=("Arial", 25), command=signUp)
btnSignUp.place(relx=0.3, rely=0.5)

root.mainloop()


