from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from course import CourseClass
from student import studentclass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import sqlite3
import os
class RMS: 
    def __init__(self,root):
        self.root=root
        self.root.title("Student Reselt Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #==icons==
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_p.png")
        #==title==

        title=Label(self.root,text="Result Management System",padx=10,compound=LEFT,image=self.logo_dash,font=("Arial",22,"bold"),bg="#1F2937",fg="white").place(x=0,y=0,relwidth=1,height=60)

        #==menu==
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.exit_).place(x=1120,y=5,width=200,height=40)

        #=====content_window=====

        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920,350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=220, y=180, width=920, height=350)

        #==Details==
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]",font=("Segoe UI",18,"bold"),bd=0,bg="#3B82F6",fg="white")
        self.lbl_student.place(x=220,y=530,width=300,height=100)

        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("Segoe UI",18,"bold"),bd=0,bg="#3B82F6",fg="white")
        self.lbl_course.place(x=530,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]",font=("Segoe UI",18,"bold"),bd=0,bg="#3B82F6",fg="white")
        self.lbl_result.place(x=840,y=530,width=300,height=100)


         #==footer==
        footer=Label(self.root,text="© 2026 Student Result Management System | Developed by Souvik Rakshit\nFor any technical issue, contact us: +91 9635245249",font=("Segoe UI",10),bg="#0F172A",fg="#E5E7EB",justify=CENTER).pack(side=BOTTOM,fill=X)

        self.update_details()
#===================================================

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{len(cr)}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{len(cr)}]")

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{len(cr)}]")

            self.root.after(1000, self.update_details)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

        finally:
            con.close()


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentclass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to Logout?",parent=self.root)
        if op==True:
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()
