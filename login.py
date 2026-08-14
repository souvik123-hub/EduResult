from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #===Bg Image===
        self.bg = ImageTk.PhotoImage(file="images/loginbg.png")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1
        )

        #============================frames
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=80,y=50)

        email=Label(login_frame,text="Email Address",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=80,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=80,y=180,width=350,height=35)

        pass_=Label(login_frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=80,y=250)
        self.txt_pass_=Entry(login_frame,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=80,y=280,width=350,height=35)

        btn_reg=Button(login_frame,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2",command=self.register_window).place(x=80,y=320)

        btn_login=Button(login_frame,text="Login",font=("times new roman",20),fg="white",bg="#B00857",cursor="hand2",command=self.login).place(x=80,y=360,height=40)

        #==footer==
        footer=Label(self.root,text="© 2026 Student Result Management System | Developed by Souvik Rakshit\nFor any technical issue, contact us: +91 9635245249",font=("Segoe UI",10),bg="#0F172A",fg="#E5E7EB",justify=CENTER).pack(side=BOTTOM,fill=X)
        
#======================================


    def register_window(self):
        self.root.destroy()
        import register



    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get(),))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Invalid USERNAME OR PASSWORD",parent=self.root)  
                else:
                   messagebox.showinfo("Success","Welcome To Result Management System",parent=self.root)
                   self.root.destroy()
                   os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)


root=Tk()
obj=login(root)
root.mainloop()