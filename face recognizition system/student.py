from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import numpy as np
class Student:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("face Recognition System ")

       self.var_id=StringVar()
       self.var_name=StringVar()
       self.var_regd = StringVar()

       img=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img1.jpeg")
       img=img.resize((500,130))
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)

       img1=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img2.jpg")
       img1=img1.resize((500,130))
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=500,height=130)

       img2=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img3.jpeg")
       img2=img2.resize((500,130))
       self.photoimg2=ImageTk.PhotoImage(img2)
       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=500,height=130)

       img3=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/b2.jpg")
       img3=img3.resize((1530,710))
       self.photoimg3=ImageTk.PhotoImage(img3)
       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)

       title_lbl=Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="white",fg="red")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       main_frame=Frame(bg_img,bd=2,bg="white")
       main_frame.place(x=10,y=55,width=1500,height=600)

       Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
       Left_frame.place(x=10,y=10,width=730,height=580)

       img_left=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/std.jpg")
       img_left=img_left.resize((500,130))
       self.photoimg_left=ImageTk.PhotoImage(img_left)
       f_lbl=Label(Left_frame,image=self.photoimg_left)
       f_lbl.place(x=5,y=0,width=720,height=130)

       class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student information",font=("times new roman",12,"bold"))
       class_student_frame.place(x=5,y=250,width=720,height=300)

       studentId_label=Label(class_student_frame,text="PHOTO ID",font=("times new roman",13,"bold"),bg="white")
       studentId_label.grid(row=0,column=0,padx=10,sticky=W)

       studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
       studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

       roll_no_label=Label(class_student_frame,text="REGD NO.",font=("times new roman",13,"bold"),bg="white")
       roll_no_label.grid(row=1,column=0,padx=10,sticky=W)
       
       roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_regd,width=20,font=("times new roman",13,"bold"))
       roll_no_entry.grid(row=1,column=1,padx=10,sticky=W)

       studentName_label=Label(class_student_frame,text="STUDENT NAME",font=("times new roman",13,"bold"),bg="white")
       studentName_label.grid(row=2,column=0,padx=10,sticky=W)

       studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
       studentName_entry.grid(row=2,column=1,padx=10,sticky=W)

       


       self.var_radio1=StringVar()
       radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
       radiobtn1.grid(row=3,column=0)
       
    #    radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
    #    radiobtn2.grid(row=3,column=1)

       btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
       btn_frame.place(x=0,y=200,width=715,height=70)

       save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       save_btn.grid(row=0,column=0)

       update_btn=Button(btn_frame,command=self.update_data,text="update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       update_btn.grid(row=0,column=1)

       delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       delete_btn.grid(row=0,column=2)

       reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       reset_btn.grid(row=0,column=3)

       btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
       btn_frame1.place(x=0,y=235,width=715,height=35)
       take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Add photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       take_photo_btn.grid(row=0,column=0)

       update_photo_btn=Button(btn_frame1,text="update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       update_photo_btn.grid(row=0,column=1)

       Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",12,"bold"))
       Right_frame.place(x=750,y=100,width=720,height=580)
       
       img_right=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img4.jpg")
       img_right=img_right.resize((720,130))
       self.photoimg_right=ImageTk.PhotoImage(img_right)
       f_lbl=Label(Right_frame,image=self.photoimg_right)
       f_lbl.place(x=5,y=0,width=720,height=130)

       Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
       Search_frame.place(x=5,y=150,width=710,height=70)
       
       search_label=Label(Search_frame,text="Search by",font=("times new roman",13,"bold"),bg="red",fg="white")
       search_label.grid(row=0,column=0,padx=10,sticky=W)
       
       search_combo=ttk.Combobox(Search_frame,font=("times new roman",15,"bold"),state="readonly",width=15)
       search_combo["values"]=("select","student id","name")
       search_combo.current(0)
       search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

       search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
       search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
       
       search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       search_btn.grid(row=0,column=3,padx=4)

       showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white",cursor="hand2")
       showAll_btn.grid(row=0,column=4,padx=4)

       table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
       table_frame.place(x=5,y=210,width=710,height=350)

       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       self.student_table=ttk.Treeview(table_frame,column=("id","regd","name","photosample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=BOTTOM,fill=Y)
       scroll_x.config(command=self.student_table.xview)
       scroll_y.config(command=self.student_table.yview)

       self.student_table.heading("id",text="Photo_Id")
       self.student_table.heading("regd",text="Regd. No")
       self.student_table.heading("name",text="Student_Name")
       self.student_table.heading("photosample",text="Photo Sample")
       self.student_table["show"]="headings"

       self.student_table.column("id",width=100)
       self.student_table.column("regd",width=100)
       self.student_table.column("name",width=100)
       self.student_table.column("photosample",width=100)

       self.student_table.pack(fill=BOTH,expand=1)
       self.student_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data()

    def add_data(self):
       if(self.var_id.get()=="" or self.var_name.get()=="" or self.var_regd ==""):
          messagebox.showerror("Error!", "All fields  are required",parent=self.root)
       else :
            try:
                  conn=mysql.connector.connect(host="localhost",username="root",password="Mdeva@2004",database="face_recognizer")
                  my_cursor=conn.cursor()
                  my_cursor.execute("insert into student values(%s,%s,%s,%s)",(
                     self.var_id.get(),
                     self.var_regd.get(),
                     self.var_name.get(),
                     self.var_radio1.get()
                     
                  ))
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo("success","student details has been added successfully",parent=self.root)
            except Exception as es:
                  messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Mdeva@2004",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()
         
         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()  
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_id.set(data[0])
        self.var_regd.set(data[1])
        self.var_name.set(data[2])
        self.var_radio1.set(data[3])

    def update_data(self):
        if(self.var_id.get()=="" or self.var_name.get()=="" ):
          messagebox.showerror("Error!", "All feilds  are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","do you want to update this student details",parent=root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mdeva@2004",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set  roll_no = %s,student_name=%s,photosample=%s where student_id=%s",(
                                  self.var_regd.get(),
                                  self.var_name.get(),
                                  self.var_radio1.get(),
                                  self.var_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mdeva@2004",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_id.set("")
        self.var_regd.set("")
        self.var_name.set("")
        self.var_radio1.set("")

    #  Generate data set Take Photo Samples

    def generate_dataset(self):
        if self.var_name.get()=="" or self.var_id.get() =="" or self.var_regd.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                conn = mysql.connector.connect(host = "localhost",username="root",password="Mdeva@2004",database="face_recognizer")

                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set roll_no=%s,student_name=%s,photosample=%s where student_id=%s",(
                                  self.var_regd.get(),
                                  self.var_name.get(),
                                  self.var_radio1.get(),
                                  self.var_id.get()
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                    

                def face_cropped(img):
                            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            faces = face_classifier.detectMultiScale(gray,1.3,5)

                            for(x,y,w,h) in faces:
                                face_cropped = img[y:y+h,x:x+w]
                                return face_cropped
                            
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                                ret,my_frame = cap.read()
                                if face_cropped(my_frame) is not None:
                                    img_id+=1
                                    face = cv2.resize(face_cropped(my_frame),(450,450))
                                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                    file_name_path= "data/user."+str(id)+"."+str(img_id)+".jpg"
                                    cv2.imwrite(file_name_path,face)
                                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                    cv2.imshow("Cropped Face",face)

                                if cv2.waitKey(1)==13 or int(img_id)==30:
                                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed!!!")
             except Exception as es:
                                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
       

     

       






if __name__ =="__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()