from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class CourseClass: 
    def __init__(self,root):
        self.root=root
        self.root.title("Student Reselt Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.root.focus_force()
    #==title
        title=Label(self.root,text="Manage Course Details",font=("Segoe UI",20,"bold"),bg="#0F172A",fg="white").place(relx=0.5,y=15,anchor="n",width=2000,height=50)
#==footer==
        footer=Label(self.root,text="© 2026 Student Result Management System | Developed by Souvik Rakshit\nFor any technical issue, contact us: +91 9635245249",font=("Segoe UI",10),bg="#0F172A",fg="#E5E7EB",justify=CENTER).pack(side=BOTTOM,fill=X)
        
    #==variables
        self.var_course=StringVar()
        self.var_duration=StringVar()
        self.var_charges=StringVar()


    #==widgets
        lbl_courseName=Label(self.root,text="Course Name",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=20,y=80)
        lbl_duration=Label(self.root,text="Duration",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=20,y=130)
        lbl_charges=Label(self.root,text="Charges",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=20,y=180)
        lbl_description=Label(self.root,text="Description",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=20,y=230)

    #==Entry Fields
        self.txt_courseName=Entry(self.root,textvariable=self.var_course,font=("Segoe UI",13,"bold"),bg="lightyellow",fg="#1F2937")
        self.txt_courseName.place(x=150,y=80,width=200)
        txt_duration=Entry(self.root,textvariable=self.var_duration,font=("Segoe UI",13,"bold"),bg="lightyellow",fg="#1F2937").place(x=150,y=130,width=200)
        txt_charges=Entry(self.root,textvariable=self.var_charges,font=("Segoe UI",13,"bold"),bg="lightyellow",fg="#1F2937").place(x=150,y=180,width=200)
        self.txt_description=Text(self.root,font=("Segoe UI",13,"bold"),bg="lightyellow",fg="#1F2937")
        self.txt_description.place(x=150,y=230,width=500,height=130)

    #==buttons
        self.btn_add=Button(self.root,text="save",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_update=Button(self.root,text="update",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.update)
        self.btn_update.place(x=270,y=400,width=110,height=40)
        self.btn_delete=Button(self.root,text="delete",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.delete)
        self.btn_delete.place(x=390,y=400,width=110,height=40)
        self.btn_clear=Button(self.root,text="clear",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.clear)
        self.btn_clear.place(x=510,y=400,width=110,height=40)

    #==search panel
        self.var_search=StringVar()
        lbl_search_courseName=Label(self.root,text="Course Name",font=("Segoe UI",13,"bold"),bg="white",fg="#1F2937").place(x=720,y=80)
        txt_search_courseName=Entry(self.root,textvariable=self.var_search,font=("Segoe UI",13,"bold"),bg="lightyellow",fg="#1F2937").place(x=870,y=80,width=180)
        btn_search=Button(self.root,text="search",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand1",command=self.search).place(x=1070,y=80,width=120,height=28)

    #==content
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=120,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    
#========================================
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0', END)
        self.txt_courseName.config(state=NORMAL)

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select course from the list first",parent=self.root)
                else: 
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("delete from course where name=?", (self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")                  


    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        # print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        # self.var_course.set(row[4])
        self.txt_description.delete('1.0', END)
        self.txt_description.insert(END, row[4])

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error","Course Name should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Course name already present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,charges,description) values(?,?,?,?)",(
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                cur.execute("select *from course")
                rows=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('', END, values=row)     
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                cur.execute(f"SELECT * FROM course WHERE name LIKE '%{self.var_search.get()}%'")
                rows=cur.fetchall()
                self.CourseTable.delete(*self.CourseTable.get_children())
                for row in rows:
                    self.CourseTable.insert('', END, values=row)     
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")


    def update(self):
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            try:
                if self.var_course.get() == "":
                    messagebox.showerror("Error","Course Name should be required", parent=self.root)
                else:
                    cur.execute("select * from course where name=?",(self.var_course.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("Error","Select course from list",parent=self.root)
                    else:
                        cur.execute("update course set duration=?,charges=?,description=? where name=?",(                    
                        self.var_duration.get(),
                        self.var_charges.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Update Successfully",parent=self.root)
                    self.show()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()