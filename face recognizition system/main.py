from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance


class Face_Recognition_System:
    def __init__(self,root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("face Recognition System ")
 
       img=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img2.jpg")
       img=img.resize((500,130))
       self.photoimg=ImageTk.PhotoImage(img)

       f_lbl=Label(self.root,image=self.photoimg)
       f_lbl.place(x=0,y=0,width=500,height=130)

       img1=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img1.jpeg")
       img1=img1.resize((500,130))
       self.photoimg1=ImageTk.PhotoImage(img1)

       f_lbl=Label(self.root,image=self.photoimg1)
       f_lbl.place(x=500,y=0,width=500,height=130)

       img2=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/img3.jpeg")
       img2=img2.resize((500,130))
       self.photoimg2=ImageTk.PhotoImage(img2)
       f_lbl=Label(self.root,image=self.photoimg2)
       f_lbl.place(x=1000,y=0,width=500,height=130)

       img3=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/bgs.jpg")
       img3=img3.resize((1530,710))
       self.photoimg3=ImageTk.PhotoImage(img3)
       bg_img=Label(self.root,image=self.photoimg3)
       bg_img.place(x=0,y=130,width=1530,height=710)

       title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
       title_lbl.place(x=0,y=0,width=1530,height=45)

       img4=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/std.jpg")
       img4=img4.resize((220,220))
       self.photoimg4=ImageTk.PhotoImage(img4)
      
       b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
       b1.place(x=200,y=100,width=220,height=220)

       b1_1=Button(bg_img,text="STUDENT DETAILS",cursor="hand2",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=200,y=300,width=220,height=40)

       img5=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/aaa.jpeg")
       img5=img5.resize((220,220))
       self.photoimg5=ImageTk.PhotoImage(img5)  
       b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
       b1.place(x=500,y=100,width=220,height=220)
       b1_1=Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=500,y=300,width=220,height=40)

       img6=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/attendance.jpg")
       img6=img6.resize((220,220))
       self.photoimg6=ImageTk.PhotoImage(img6)  
       b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
       b1.place(x=800,y=100,width=220,height=220)
       b1_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=800,y=300,width=220,height=40)

       img7=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/train.jpg")
       img7=img7.resize((220,220))
       self.photoimg7=ImageTk.PhotoImage(img7)  
       b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.train_data)
       b1.place(x=1100,y=100,width=220,height=220)
       b1_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
       b1_1.place(x=1100,y=300,width=220,height=40)

    def student_details(self):
          self.new_window=Toplevel(self.root)
          self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)

        


if __name__ =="__main__":
   root=Tk()
   obj=Face_Recognition_System(root)
   root.mainloop()