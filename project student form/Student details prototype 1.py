# needs combobox,message box(for error),text area
# Order of Entry
# name,age,gender,address,dob,adyear,email,fathername,mothername,course
#use combobox for dob
#
#
#
#


 
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *
import csv

root=Tk()
root.title("Student form")
root.geometry("1590x800")
root.minsize(1590,800)
root.maxsize(1590,800)

v=Scrollbar(root,orient="vertical")
v.pack(side=RIGHT,fill='y')
    
frame=Frame(root,bg="#ffffe6",height=800,width=1573)
frame.place(x=0,y=0)
frame.grid_propagate(0)

frame1=Frame(frame,bg="blue")
frame1.place(x=50,y=100)


head=Label(frame,bg="#ffffe6",fg="blue" ,text="Student Details",font=("Arial Bold",18))
head.place(x=700,y=30)

lbl=list()
def backed1():
    global lbl
    with open("Student2.csv",mode="r") as myfile:
        read=csv.reader(myfile)
        i=0
        for row in read:
            if i==0:
                lbl.append(Label(frame1,text=row[0],bg="#baffdf",borderwidth=2,relief=SOLID,width=5,padx=2,pady=2))
                lbl[(i*12)].grid(row=i,column=1)
                lbl.append(Label(frame1,text=row[1],bg="#baffdf",borderwidth=2,relief=SOLID,width=20,padx=2,pady=2))
                lbl[(i*12)+1].grid(row=i,column=2)
                lbl.append(Label(frame1,text=row[2],bg="#baffdf",borderwidth=2,relief=SOLID,width=5,padx=2,pady=2))
                lbl[(i*12)+2].grid(row=i,column=3)
                lbl.append(Label(frame1,text=row[3],bg="#baffdf",borderwidth=2,relief=SOLID,width=12,padx=2,pady=2))
                lbl[(i*12)+3].grid(row=i,column=4)
                lbl.append(Label(frame1,text=row[4],bg="#baffdf",borderwidth=2,relief=SOLID,width=15,padx=2,pady=2))
                lbl[(i*12)+4].grid(row=i,column=5)
                lbl.append(Label(frame1,text=row[5],bg="#baffdf",borderwidth=2,relief=SOLID,width=18,padx=2,pady=2))
                lbl[(i*12)+5].grid(row=i,column=6)
                lbl.append(Label(frame1,text=row[6],bg="#baffdf",borderwidth=2,relief=SOLID,width=18,padx=2,pady=2))
                lbl[(i*12)+6].grid(row=i,column=7)
                lbl.append(Label(frame1,text=row[7],bg="#baffdf",borderwidth=2,relief=SOLID,width=15,padx=2,pady=2))
                lbl[(i*12)+7].grid(row=i,column=8)
                lbl.append(Label(frame1,text=row[8],bg="#baffdf",borderwidth=2,relief=SOLID,width=12,padx=2,pady=2))
                lbl[(i*12)+8].grid(row=i,column=9)
                lbl.append(Label(frame1,text=row[9],bg="#baffdf",borderwidth=2,relief=SOLID,width=47,padx=2,pady=2))
                lbl[(i*12)+9].grid(row=i,column=10)
                lbl.append(Label(frame1,text=row[10],bg="#baffdf",borderwidth=2,relief=SOLID,width=15,padx=2,pady=2))
                lbl[(i*12)+10].grid(row=i,column=11)
                lbl.append(Label(frame1,text=row[11],bg="#baffdf",borderwidth=2,relief=SOLID,width=18,padx=2,pady=2))
                lbl[(i*12)+11].grid(row=i,column=12)

            else:
                lbl.append(Label(frame1,text=row[0],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=5,padx=2,pady=2))
                lbl[(i*12)].grid(row=i,column=1)
                lbl.append(Label(frame1,text=row[1],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=20,padx=2,pady=2,wraplength=370))
                lbl[(i*12)+1].grid(row=i,column=2)
                lbl.append(Label(frame1,text=row[2],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=5,padx=2,pady=2))
                lbl[(i*12)+2].grid(row=i,column=3)
                lbl.append(Label(frame1,text=row[3],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=12,padx=2,pady=2))
                lbl[(i*12)+3].grid(row=i,column=4)
                lbl.append(Label(frame1,text=row[4],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=15,padx=2,pady=2,wraplength=107))
                lbl[(i*12)+4].grid(row=i,column=5)
                lbl.append(Label(frame1,text=row[5],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=18,padx=2,pady=2,wraplength=128))
                lbl[(i*12)+5].grid(row=i,column=6)
                lbl.append(Label(frame1,text=row[6],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=18,padx=2,pady=2,wraplength=128))
                lbl[(i*12)+6].grid(row=i,column=7)
                lbl.append(Label(frame1,text=row[7],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=15,padx=2,pady=2,wraplength=107))
                lbl[(i*12)+7].grid(row=i,column=8)
                lbl.append(Label(frame1,text=row[8],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=12,padx=2,pady=2))
                lbl[(i*12)+8].grid(row=i,column=9)
                lbl.append(Label(frame1,text=row[9],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=47,padx=2,pady=2, wraplength=370))
                lbl[(i*12)+9].grid(row=i,column=10)
                lbl.append(Label(frame1,text=row[10],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=15,padx=2,pady=2))
                lbl[(i*12)+10].grid(row=i,column=11)
                lbl.append(Label(frame1,text=row[11],bg="#a9ffa6",borderwidth=2,height=2,relief=SOLID,width=18,padx=2,pady=2))
                lbl[(i*12)+11].grid(row=i,column=12)
            i+=1
    return


#def backed2():
#    global lbl
#    with open("Student2.csv",mode="r") as myfile:
#        read=csv.reader(myfile)
#        i=0
#        for row in read:
#            lbl.append(Label(frame1,text="",bg="#ffffe6",width=11,padx=2,pady=2))
#            lbl[(i*13)].grid(row=i,column=0)
#            lbl.append(Label(frame1,text=row[0],bg="#ffffe6",width=12,padx=2,pady=2))
#            lbl[(i*13)].grid(row=i,column=1)
#            lbl.append(Label(frame1,text=row[1],bg="#ffffe6"))
#            lbl[(i*13)+1].grid(row=i,column=2)
#            lbl.append(Label(frame1,text=row[2],bg="#ffffe6"))
#            lbl[(i*13)+2].grid(row=i,column=3)
#            lbl.append(Label(frame1,text=row[3],bg="#ffffe6"))
#            lbl[(i*13)+3].grid(row=i,column=4)
#            lbl.append(Label(frame1,text=row[4],bg="#ffffe6"))
#            lbl[(i*13)+4].grid(row=i,column=5)
#            lbl.append(Label(frame1,text=row[5],bg="#ffffe6"))
#            lbl[(i*13)+5].grid(row=i,column=6)
#            lbl.append(Label(frame1,text=row[6],bg="#ffffe6"))
#            lbl[(i*13)+6].grid(row=i,column=7)
#            lbl.append(Label(frame1,text=row[7],bg="#ffffe6"))
#            lbl[(i*13)+7].grid(row=i,column=8)
#            lbl.append(Label(frame1,text=row[8],bg="#ffffe6"))
#            lbl[(i*13)+8].grid(row=i,column=9)
#            lbl.append(Label(frame1,text=row[9],bg="#ffffe6"))
#            lbl[(i*13)+9].grid(row=i,column=10)
#            lbl.append(Label(frame1,text=row[10],bg="#ffffe6"))
#            lbl[(i*13)+10].grid(row=i,column=11)
#            lbl.append(Label(frame1,text=row[11],bg="#ffffe6"))
#            lbl[(i*13)+11].grid(row=i,column=12)
#            i+=1
#  
#       return

backed1()





root.mainloop()
