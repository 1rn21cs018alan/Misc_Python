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

root=Tk()
root.title("Student form")
root.geometry("500x800")
root.minsize(500,800)
root.maxsize(500,800)



UID=10800
studentlist=list()
def submit():
    global UID
    
    name=optname.get()
    age=ageval.get()
    gender=genval.get()
    address=optaddress.get()
    dob=optdob.get()
    adyear=optadyear.get()
    email=optemail.get()
    fathername=optfathername.get()
    mothername=optmothername.get()
    course=crsval.get()
    number=optnumber.get()
    print(name,age,gender,address,dob,adyear,email,fathername,mothername,number,course)

    if check1(name) and checkage(age) and checkcrs(course) and checkgen(gender) and checkad(adyear) and check1(dob):
        if not check1(address):
            address="N/A"
        if not check1(fathername):
            fathername="N/A"
        if not check1(mothername):
            mothername="N/A"
        if not check1(email):
            email="N/A"
        if check1(number):
            if int(number)<=999999999 or int(number)>=9999999999:
                messagebox.showerror(title="Invalid Number",message="Enter The Phone Number Properly")
                return
        else:
            number="N/A"
        if not check1(address):
            address="N/A"
        print(name,age,gender,address,dob,adyear,email,fathername,mothername,number,course)
        UID+=1
        studentlist.append(student(name,age,gender,address,dob,adyear,email,fathername,mothername,number,course))
        reset()
    else:
        messagebox.showerror(title="Wrong Information",message="Fill the Mandatory Fields Properly \n(Name,Age,Gender,DOB,Year of Admission and Course )")
    return

def check1(a):
    if a=="":
        return False
    else:
        return True

def checkage(a):
    if a=="Select Age":
        return False
    else:
        return True

    
def checkcrs(a):
    if a=="Select Course":
        return False
    else:
        return True

    
def checkgen(a):
    if a=="Select Gender":
        return False
    else:
        return True

def checkad(a):
    if a=="":
        return False
    else:
        if int(a) not in range(2000,2023):
            return False            
        return True
    

def reset():
    setage()
    setgen()
    setcrs()
    optname.delete(0,END)
    optaddress.delete(0,END)
    optdob.delete(0,END)
    optadyear.delete(0,END)
    optemail.delete(0,END)
    optfathername.delete(0,END)
    optmothername.delete(0,END)
    optnumber.delete(0,END)    
    return

    
class student():
    
    def __init__(self,name,age,gender,address,dob,adyear,email,fathername,mothername,number,course):
        global UID
        self.UID=UID
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
        self.dob=dob
        self.adyear=adyear
        self.email=email
        self.fathername=fathername
        self.mothername=mothername
        self.number=number
        self.course=course

frame=Frame(root,bg="#dcebff",height=800,width=500)
frame.grid(row=0,column=0)
frame.grid_propagate(0)



LBLname=Label(frame,bg="#dcebff",text="Enter Name :",font=("Arial",12),anchor="e",width=20)    #imp
LBLname.grid(row=2 ,column=1)

LBLage=Label(frame,bg="#dcebff",text="Enter Age :",font=("Arial",12),anchor="e",width=20)      #imp
LBLage.grid(row=3,column=1)

LBLgender=Label(frame,bg="#dcebff",text="Enter Gender :",font=("Arial",12),anchor="e",width=20)        #imp
LBLgender.grid(row=4,column=1)

LBLdob=Label(frame,bg="#dcebff",text="Enter Date Of Birth :",font=("Arial",12),anchor="e",width=20)   #use combo box for dob,imp
LBLdob.grid(row=5,column=1)


LBLemail=Label(frame,bg="#dcebff",text="Enter Email Address :",font=("Arial",12),anchor="e",width=20)
LBLemail.grid(row=6,column=1)

LBLfathername=Label(frame,bg="#dcebff",text="Enter Father's Name :",font=("Arial",12),anchor="e",width=20)
LBLfathername.grid(row=7,column=1)

LBLmothername=Label(frame,bg="#dcebff",text="Enter Mother's Name :",font=("Arial",12),anchor="e",width=20)
LBLmothername.grid(row=8,column=1)

LBLnumber=Label(frame,bg="#dcebff",text="Enter Phone Number :",font=("Arial",12),anchor="e",width=20)
LBLnumber.grid(row=9,column=1)

LBLaddress=Label(frame,bg="#dcebff",text="Enter Address :",font=("Arial",12),anchor="e",width=20)
LBLaddress.grid(row=10,column=1)

LBLadyear=Label(frame,bg="#dcebff",text="Enter Year of Admission :",font=("Arial",12),anchor="e",width=20)     #imp
LBLadyear.grid(row=11,column=1)

LBLcourse=Label(frame,bg="#dcebff",text="Choose Current course :",font=("Arial",12),anchor="e",width=20)       #imp
LBLcourse.grid(row=12,column=1)

head=Label(frame,bg="#dcebff",fg="white" ,text="Student Details",font=("Arial Bold",18))
head.place(x=150,y=30)

empty0=Label(frame,bg="#dcebff",text="  ",height=2)
empty0.grid(row=0,column=0)
empty1=Label(frame,bg="#dcebff",text="   ",height=2)
empty1.grid(row=1,column=0)
empty2=Label(frame,bg="#dcebff",text="   ",height=2)
empty2.grid(row=2,column=0)
empty3=Label(frame,bg="#dcebff",text="   ",height=2)
empty3.grid(row=3,column=0)
empty4=Label(frame,bg="#dcebff",text="   ",height=2)
empty4.grid(row=4,column=0)
empty5=Label(frame,bg="#dcebff",text="   ",height=2)
empty5.grid(row=5,column=0)
empty6=Label(frame,bg="#dcebff",text="   ",height=2)
empty6.grid(row=6,column=0)
empty7=Label(frame,bg="#dcebff",text="   ",height=2)
empty7.grid(row=7,column=0)
empty8=Label(frame,bg="#dcebff",text="   ",height=2)
empty8.grid(row=8,column=0)
empty9=Label(frame,bg="#dcebff",text="   ",height=2)
empty9.grid(row=9,column=0)
empty10=Label(frame,bg="#dcebff",text="   ",height=2)
empty10.grid(row=10,column=0)
empty11=Label(frame,bg="#dcebff",text="   ",height=2)
empty11.grid(row=11,column=0)
empty12=Label(frame,bg="#dcebff",text="   ",height=2)
empty12.grid(row=12,column=0)
empty13=Label(frame,bg="#dcebff",text="   ",height=2)



optname=Entry(frame,width=40)
optname.grid(row=2,column=2)

ageval=StringVar()
optage=Combobox(frame,textvariable=ageval,state='readonly')
optage['values']=['16','17','18','19','20']
def setage():
    global ageval
    ageval.set("Select Age")
    return
setage()
optage.place(x=202,y=116)

genval=StringVar()
optgen=Combobox(frame,textvariable=genval,state='readonly')
optgen['values']=["Male","Female","Gender-Fluid"]
def setgen():
    global genval
    genval.set('Select Gender')
    return
setgen()
optgen.place(x=202,y=152)

optdob=Entry(frame,width=40)
optdob.grid(row=5,column=2)

optemail=Entry(frame,width=40)
optemail.grid(row=6,column=2)

optfathername=Entry(frame,width=40)
optfathername.grid(row=7,column=2)

optmothername=Entry(frame,width=40)
optmothername.grid(row=8,column=2)


optnumber=Entry(frame,width=40)
optnumber.grid(row=9,column=2)

optaddress=Entry(frame,width=40)
optaddress.grid(row=10,column=2)

optadyear=Entry(frame,width=40)
optadyear.grid(row=11,column=2)


crsval=StringVar()
optcrs=Combobox(frame,textvariable=crsval,state='readonly')
optcrs['values']=["Computer Science","Computer Engineering"," Electronics ","AI and ML","Areospace","Aeronautical","Mechanical","Civil","Psychology","Medical"]
def setcrs():
    global crsval
    crsval.set("Select Course")
    return
setcrs()
optcrs.place(x=202,y=440)

sub=Button(frame,text="Submit",font=("Arial Bold",12),bg="white",command=submit)
sub.place(x=202,y=470)


resb=Button(frame,text="Reset",font=("Arial Bold",12),bg="white",command=reset)
resb.place(x=202,y=510)


root.mainloop()
