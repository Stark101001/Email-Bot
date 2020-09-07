from tkinter import *
from tkinter import messagebox
import time
import random
import smtplib

window = Tk()
window.geometry("600x400+500+120")
window.resizable(0, 0)
window.title("Login Portal with OTP")


class OTP:
    otp = random.randint(100000, 999999)
    Mes = str("Your One time passcode is " + str(otp))


def mail():
    Login()
    Sender_gmail = home_e1.get()
    Rec_gmail = home_e2.get()
    message = OTP.Mes

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(Sender_gmail, "Password")#Note Enter your gmail password.
    server.sendmail(Sender_gmail, Rec_gmail, message)
    server.quit()


def Log_but():
    if log_e1.get() == OTP.otp:
        messagebox.showinfo("Info", "Login Successfull with Otp")
        log_e1.set("")
    else:
        messagebox.showerror("Error", "Invalid OTP")


def About():
    f_about = Frame(bg="black")
    f_about.place(x=0, y=0, width=600, height=400)

    # l_Email=Label(f_about,text="\n\n\n",bg='black',font=(None,30),fg='lime')
    # l_Email.place(x=0,y=10)

    l_Email = Label(f_about,
                    text="Starkdsuoza786@gmail.com\n\nPawan Kumar\n\nhttps://github.com/Stark101001\n\n7710555102",
                    bg='black', font=('monaco', 20, 'bold'), fg='#7F38EC')
    l_Email.place(x=50, y=10)

    l_Email = Label(f_about, text="☻", bg='black', font=(None, 120), fg='lime')
    l_Email.place(x=220, y=225)

    but = Button(f_about, text='Back', fg='black', bg='lime', width=10, command=Login)
    but.place(x=2, y=2)


log_e1 = IntVar()


# =================================Second Window=====================================
def Login():
    f2_login = Frame(bg='black')
    f2_login.place(x=0, y=0, width=600, height=400)

    l01_login = Label(f2_login, text="The OTP has been sent to \nYou'r Gmail ID", fg='#eac117', bg='black',
                      font=('monaco', 20, 'bold'))
    l01_login.place(x=90, y=80)

    l0_login = Label(f2_login, text="―", width="600", bg='lime')
    l0_login.place(x=0, y=50)

    l1_login = Label(f2_login, text=" OTP LoginSetup  ", fg='red', font=('monaco', 38, 'bold'), bg='black')
    l1_login.place(x=0, y=5)

    l2_ligin = Label(f2_login, text="Enter_Otp", font=('monaco', 20, 'bold'), bg='black', fg='lime')
    l2_ligin.place(x=60, y=170)

    l2_ligin = Label(f2_login, text=":", font=('monaco', 18, 'bold'), bg='black', fg='lime')
    l2_ligin.place(x=220, y=178)

    e1_login = Entry(f2_login, width=20, textvariable=log_e1, fg="black", bd=5, bg="#D1D0CE",
                     font=('monaco', 15, 'bold'))
    e1_login.place(x=280, y=170)

    b2_login = Button(f2_login, text="Submit", bg='green', bd=5, fg='yellow', width=13, height=2, command=Log_but)
    b2_login.place(x=180, y=260)

    b1_login = Button(f2_login, text="Resend Otp", bg='#ff2400', width=13, height=2, bd=3, command=mail)
    b1_login.place(x=300, y=260)

    b4_login = Button(f2_login, text="About", bg='#0C4DF2', width=10, height=2, command=About)
    b4_login.place(x=515, y=354)

    b5_login = Button(f2_login, text="Home", bg='#0C4DF2', width=10, height=2, command=Home)
    b5_login.place(x=7, y=354)


home_e1 = StringVar()
home_e2 = StringVar()


def Home():
    f1_home = Frame(bg='black')
    f1_home.place(x=0, y=0, width=600, height=400)

    l5_home = Label(f1_home, text="Sender_Email►", font=('monaco', 20, 'bold'), bg='black', fg='lime')
    l5_home.place(x=60, y=170)

    l6_home = Label(f1_home, text="Reci_Email►", font=('monaco', 20, 'bold'), bg='black', fg='lime')
    l6_home.place(x=95, y=220)

    e1_home = Entry(f1_home, width=20, textvariable=home_e1, fg="black", bd=3, bg="#D1D0CE",
                    font=('monaco', 15, 'bold'))
    e1_home.place(x=280, y=170)

    e2_home = Entry(f1_home, width=20, textvariable=home_e2, fg="black", bd=3, bg="#D1D0CE",
                    font=('monaco', 15, 'bold'))
    e2_home.place(x=280, y=220)

    b1_home = Button(f1_home, text='Send', bg="lime", width=15, height=2, command=mail)
    b1_home.place(x=230, y=290)

    l2_home = Label(f1_home, height=1, bg='black')
    l2_home.pack(fill=X)

    l4_home = Label(f1_home, text="―", width="600", bg='lime')
    l4_home.place(x=0, y=50)

    l1_home = Label(f1_home, text=" OTP LoginSetup  ", fg='red', font=('monaco', 38, 'bold'), bg='black')
    l1_home.place(x=0, y=5)

    l7_home = Label(f1_home, text="EmailBot", font=('monaco', 45, 'bold'), bg='black', fg='#7F38EC')
    l7_home.place(x=120, y=80)

    l3_home = Label(f1_home, bg='black', fg='green', text='MR.Pawan Kumar', font=('monaco', 14, 'bold'))
    l3_home.place(x=440, y=375)


Home()

window.mainloop()
