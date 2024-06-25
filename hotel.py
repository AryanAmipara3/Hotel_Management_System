from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom
import subprocess
from feedback import Feedback

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # =================fist img=================

        img1=Image.open(r"----enter your path here----\hotel_management\hotel images\h.webp") # enter path of your file
        img1=img1.resize((1537,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1537,height=140)

        # =================logo====================

        img2=Image.open(r"----enter your path here----\hotel_management\hotel images\llogo.webp") # enter path of your file
        img2=img2.resize((230,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)

        # ===============title================

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="blue",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1537,height=50)

        # ===============main Frame====================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1537,height=620)

        # =======================menu==================

        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230,height=35)

        # ===============btn Frame====================
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE,cursor="hand2")
        btn_frame.place(x=0,y=35,width=230,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="orange",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="red",bd=0,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="green",bd=0,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        feedback_btn=Button(btn_frame,text="FEEDBACK",command=self.feedback,width=22,font=("times new roman",14,"bold"),bg="black",fg="yellow",bd=0,cursor="hand2")
        feedback_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="grey",bd=0,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)


        # =======================right side image===================

        img3=Image.open(r"----enter your path here----\hotel_management\hotel images\taj.jpg") # enter path of your file
        img3=img3.resize((1302,598),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=230,y=0,width=1302,height=598)

        # =========================down images=====================

        img4=Image.open(r"----enter your path here----\hotel_management\hotel images\hhh.jpg") # enter path of your file
        img4=img4.resize((230,196),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=225,width=230,height=196)
        
        img5=Image.open(r"----enter your path here----\hotel_management\hotel images\food.jpeg") # enter path of your file
        img5=img5.resize((230,180),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lbling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=420,width=230,height=180)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()
        subprocess.call(["python", "login.py"])

    def feedback(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)



if __name__== "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()