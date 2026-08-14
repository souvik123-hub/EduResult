from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class reportClass: 
    def __init__(self,root):
        self.root=root
        self.root.title("Student Reselt Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
    #==title
        title=Label(self.root,text="View Student Results",font=("Segoe UI",20,"bold"),bg="orange",fg="#262626").place(relx=0.5,y=15,anchor="n",width=2000,height=50)
    #==footer==
        footer=Label(self.root,text="© 2026 Student Result Management System | Developed by Souvik Rakshit\nFor any technical issue, contact us: +91 9635245249",font=("Segoe UI",10),bg="#0F172A",fg="#E5E7EB",justify=CENTER).pack(side=BOTTOM,fill=X)
        
    #==search
        self.var_search=StringVar()
        self.var_id=""
        lbl_search=Label(self.root,text="Search by Roll Number",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("Segoe UI",13,),bg="lightyellow",fg="#1F2937").place(x=520,y=100,width=150)
        btn_search=Button(self.root,text="search",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.search).place(x=680,y=100,width=100,height=28)
        btn_clear=Button(self.root,text="clear",font=("goudy old style",15,"bold"),bg="#2ef50b",fg="white",cursor="hand1",command=self.clear).place(x=800,y=100,width=100,height=28)

    #==result table
        lbl_roll=Label(self.root,text="Roll No",font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root,text="Course",font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks=Label(self.root,text="Marks Obtained",font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full=Label(self.root,text="Total Marks",font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course=Label(self.root,font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.marks=Label(self.root,font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150,height=50)
        self.full=Label(self.root,font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("Segoe UI",13,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

    #== delete
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f50606",fg="white",cursor="hand1",command=self.delete).place(x=500,y=350,width=150,height=35)

######################################################################
    def search(self):
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                try:
                    if self.var_search.get()=="":
                        messagebox.showerror("Error","Roll No. Should be required",parent=self.root)
                    else:
                        cur.execute(f"SELECT * FROM result where roll=?",(self.var_search.get(),))
                        row=cur.fetchone()
                        if row!=None:
                            self.var_id=row[0]
                            self.roll.config(text=row[1])
                            self.name.config(text=row[2])
                            self.course.config(text=row[3])
                            self.marks.config(text=row[4])
                            self.full.config(text=row[5])
                            self.per.config(text=row[6])
                        else:
                            messagebox.showerror("Error","No Record Found",parent=self.root)   
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.marks.config(text="")
        self.full.config(text="")
        self.per.config(text="") 
        self.var_search.set("")  

    def delete(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                if self.var_id=="":
                    messagebox.showerror("Error","search student result first", parent=self.root)
                else:
                    cur.execute("select * from result where rid=?",(self.var_id,))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                    else: 
                        op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                        if op == True:
                            cur.execute("delete from result where rid=?", (self.var_id,))
                            con.commit()
                            messagebox.showinfo("Delete", "Result deleted Successfully", parent=self.root)
                            self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")    


if __name__=="__main__":
    root=Tk()
    obj=reportClass(root)
    root.mainloop()