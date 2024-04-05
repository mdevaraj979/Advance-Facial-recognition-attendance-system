from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System ")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #first image
        img_top=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/FACE.jpg")
        img_top=img_top.resize((650,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)
       

        #second image
        img_bottom=Image.open("C:/Users/HP/OneDrive/Desktop/face recognizition system/GUI_IMG/faceDec.jpg")
        img_bottom=img_bottom.resize((650,700))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
       
        #button
        b1_1=Button(f_lbl,text="Face recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)

        #attendance

    def mark_attendance(self,p,r,i):
          with open("attendence.csv","r+",newline="\n") as f:
              myDataList = f.readlines()
              name_list = []
              for line in myDataList:
                  entry = line.split((","))
                  name_list.append((entry[0]))
              if((p not in name_list) and (r not in name_list) and (i not in name_list) ):
                  now = datetime.now()
                  d1 = now.strftime("%d/%m/%Y")
                  dtString = now.strftime("%H:%M:%S")
                  f.writelines(f"\n{p},{r},{i},{dtString},{d1},Present")

                  
        
    def face_recog(self):
         

        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf) :
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100 * (1 - predict / 300)))
                print(id)
                

                conn=mysql.connector.connect(host="localhost",username="root",password="Mdeva@2004",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select student_name from student where student_id="+str(id))
                i=my_cursor.fetchone()  
                i="+".join(i)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                p=my_cursor.fetchone()
                p="+".join(p)

                my_cursor.execute("select roll_no from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                print(confidence)

                if(confidence>80):
                    cv2.putText(img,f"ID:{p}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Regd No:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(p,r,i)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,255),3)
                coord=[x,y,w,h] 

            return coord
        def recognize(img,clf,faceCascade):
            coords=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        


                    
              
   


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
