def login():
    loginFrame = Frame(root, bg="#261E4F")
    loginFrame.pack()

    def back():
        loginFrame.forget()

    btnBack = Button(loginFrame, text="BACK", bg="white", command=back)
    btnBack.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

def signUp():
    signUpFrame = Frame(root, bg="#2D4F1E")
    signUpFrame.pack()

    def back():
        signUpFrame.forget()

    btnBack = Button(signUpFrame, text="BACK", bg="white", command=lambda:back())
    btnBack.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

root.config(bg="deepskyblue")

btnLogin = Button(root, text="Login", font=("Comis Sans Ms", 25), command=login)
btnLogin.place(relx=0.35, rely=0.5, relwidth=0.3, relheight=0.15)

btnSignUp = Button(root, text="SignUp", font=("Comis Sans Ms", 25), command=signUp)
btnSignUp.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.15)