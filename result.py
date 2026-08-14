from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass: 
    def __init__(self,root):
        self.root=root
        self.root.title("Student Reselt Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
    #==title
        title=Label(self.root,text="Add Student Results",font=("Segoe UI",20,"bold"),bg="orange",fg="#262626").place(relx=0.5,y=15,anchor="n",width=2000,height=50)
#==footer==
        footer=Label(self.root,text="© 2026 Student Result Management System | Developed by Souvik Rakshit\nFor any technical issue, contact us: +91 9635245249",font=("Segoe UI",10),bg="#0F172A",fg="#E5E7EB",justify=CENTER).pack(side=BOTTOM,fill=X)
        
    #==widgets
    #==variables
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.roll_list=[]
        self.fetch_roll()

        lbl_select=Label(self.root,text="Select Student",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=50,y=100)
        lbl_name=Label(self.root,text="Name",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=50,y=160)
        lbl_course=Label(self.root,text="Course",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=50,y=220)
        lbl_marks_ob=Label(self.root,text="Marks Obtained",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=50,y=280)
        lbl_full_marks=Label(self.root,text="Full Marks",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=50,y=340)

        self.txt_student=ttk.Combobox(self.root,textvariable=self.var_roll,values=(self.roll_list),font=("Segoe UI",13,"bold"),state='readonly',justify=CENTER)
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select") 
        btn_search=Button(self.root,text="search",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.search).place(x=500,y=100,width=100,height=28)

        txt_namel=Entry(self.root,textvariable=self.var_name,font=("Segoe UI",20,"bold"),bg="lightyellow",fg="#1F2937",state="readonly").place(x=280,y=160,width=320)
        txt_course=Entry(self.root,textvariable=self.var_course,font=("Segoe UI",20,"bold"),bg="lightyellow",fg="#1F2937",state="readonly").place(x=280,y=220,width=320)
        txt_marks=Entry(self.root,textvariable=self.var_marks,font=("Segoe UI",20,"bold"),bg="lightyellow",fg="#1F2937").place(x=280,y=280,width=320)
        txt_full_marks=Entry(self.root,textvariable=self.var_full_marks,font=("Segoe UI",20,"bold"),bg="lightyellow",fg="#1F2937").place(x=280,y=340,width=320)

        #==buttons
        btn_add=Button(self.root,text="Submit",font=("times new roman",15,"bold"),bg="lightgreen",activebackground="lightgreen",cursor="hand1",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",activebackground="lightgreen",cursor="hand1",command=self.clear).place(x=430,y=420,width=120,height=35)

        #==Image
        self.bg_img = Image.open("images/result.png")
        self.bg_img = self.bg_img.resize((500,300), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=730, y=100)

#======================================
    def fetch_roll(self):
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                try:
                    cur.execute("select Roll from student")
                    rows=cur.fetchall()
                    if len(rows)>0:
                        for row in rows:
                            self.roll_list.append(row[0])                            
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                try:
                    cur.execute(f"SELECT name,course FROM student where roll=?",(self.var_roll.get(),))
                    row=cur.fetchone()
                    if row!=None:
                        self.var_name.set(row[0])
                        self.var_course.set(row[1])
                    else:
                        messagebox.showerror("Error","No Record Found",parent=self.root)   
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}")

    def add(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                if self.var_name.get() == "":
                    messagebox.showerror("Error","Please first search student record", parent=self.root)
                else:
                    cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                    row=cur.fetchone()
                    if row!=None:
                        messagebox.showerror("Error","Result already present",parent=self.root)
                    else:
                        per=(int(self.var_marks.get())*100)/int(self.var_full_marks.get())
                        cur.execute("insert into result (roll,name,course,marks_ob,full_marks,per) values(?,?,?,?,?,?)",(
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_marks.get(),
                            self.var_full_marks.get(),
                            str(per)
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_roll.set("select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_full_marks.set(""),         


if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()