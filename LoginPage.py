from tkinter import *
from tkinter import messagebox


def Loginpage(my_frame):#my_frame is root

    #sign in verification, activated when sign in button pressed, to change with database
    def signin():
        username=user.get()
        password=code.get()

        if username=='admin' and password=='1234':
            #load new screen when login successful
            screen2=Toplevel(my_frame)
            screen2.title("App")
            screen2.geometry('925x500+300+200')
            screen2.config(bg='white')

            Label(screen2, text="new screen", bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)

            screen2.mainloop()
        elif username!= 'admin' and password !='1234':
            messagebox.showerror("Invalid", "invalid username and password")
        elif password!='1234':
            messagebox.showerror("Invalid", "invalid password")
        elif username!='admin':
            messagebox.showerror("Invalid", "invalid username")


    frame=Frame(my_frame, width=350, height=350, bg="white")
    frame.place(x=70, y=70)


    heading=Label(frame, text="Sign in", fg='#57a1f8', bg="white", font=('Microsoft Yahei UI Light', 23,'bold'))
    heading.place(x=100, y=5)

    ######## user -----------------------

    #event functions
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0, 'Username')


    #user textbox
    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0,'Username')

    #event listener
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    #textbox lines
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ######## passoword -------------------
    #event functions
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0, 'Password')


    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0,'Password')

    #event listeners
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ########## sign in button ----------
    #command=sign in for login verification
    Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
    label=Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light',9))
    label.place(x=75, y=270)

    sign_up=Button(frame, width=6, text="Sign up", border=0, bg='white', cursor='hand2', fg='#57a1f8')
    sign_up.place(x=215, y=270)

    my_frame.mainloop()
    return 0