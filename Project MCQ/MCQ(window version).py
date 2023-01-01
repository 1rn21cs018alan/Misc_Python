# MCQ program prototype 1

import pyautogui
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *
import random
import time
import csv

window=Tk()
window.title("MCQ Exam")
window.attributes('-fullscreen',True)


#use backup function from mcq(csv).py
number=14    #int(input("Enter number : "))
correct=4
wrong=1



glo=0
def waiting(): # to show the frames
    fir.destroy()
    frame1.grid(row=0,column=0)
    frame2.grid(row=0,column=1)
    
    setinfo(0)
    return



#The 'answer' Frame


frame1=Frame(window,height=900,width=1300,bg="white",bd=4,highlightbackground="grey",highlightthickness=2)
frame1.grid_propagate(0)


lbl1=Label(frame1,bg="white",height=3) #question number label
lbl1.grid(row=0,column=0)
lbl2=Label(frame1,bg="white",height=5) #Question information Label
lbl2.grid(row=1,column=0)


selected=IntVar()
selects=list()

ans1=Label(frame1,bg="white")
ans2=Label(frame1,bg="white")
ans3=Label(frame1,bg="white")
ans4=Label(frame1,bg="white")
rad0=Radiobutton(frame1,bg="white",value=0,variable=selected,width=1)
rad1=Radiobutton(frame1,bg="white",value=1,variable=selected,width=1)
rad2=Radiobutton(frame1,bg="white",value=2,variable=selected,width=1)
rad3=Radiobutton(frame1,bg="white",value=3,variable=selected,width=1)
rad4=Radiobutton(frame1,bg="white",value=4,variable=selected,width=1)


# the answering interface
def setinfo(i):
    global selected,qa,selects,glo
    lbl1.configure(text=("Question "+str(quest[i].slno)),bg="white",height=3) #question number label
    lbl2.configure(text=quest[i].q,bg="white",height=5) #Question information Label
    glo=i
    if i==0:
        prevbut.config(state="disabled")
        nextbut.config(state="normal")
    elif i==(number-1):
        prevbut.config(state="normal")
        nextbut.config(state="disabled")
    else:
        prevbut.config(state="normal")
        nextbut.config(state="normal")
        
    if i not in qa:
        selected.set(None)
        qa.append(i)    
        a=[2,3,4,5]
        random.shuffle(a)
        select[i]=a        
        print(a)
        a1=int(a[0])
        a2=int(a[1])
        a3=int(a[2])
        a4=int(a[3])
        rad1.grid(column=0,row=a1)
        ans1.configure(text=quest[i].ans,bg="white")
        ans1.grid(column=1,row=a1)
        rad2.grid(column=0,row=a2)
        ans2.configure(text=quest[i].wrong1,bg="white")
        ans2.grid(column=1,row=a2)
        rad3.grid(column=0,row=a3)
        ans3.configure(text=quest[i].wrong2,bg="white")
        ans3.grid(column=1,row=a3)
        rad4.grid(column=0,row=a4)
        ans4.configure(text=quest[i].wrong3,bg="white")
        ans4.grid(column=1,row=a4)
    elif ans[i]!=2:
        selected.set(int(selects[i]))
        a1=int(select[i][0])
        a2=int(select[i][1])
        a3=int(select[i][2])
        a4=int(select[i][3])
        rad1.grid(column=0,row=a1)
        ans1.configure(text=quest[i].ans,bg="white")
        ans1.grid(column=1,row=a1)
        rad2.grid(column=0,row=a2)
        ans2.configure(text=quest[i].wrong1,bg="white")
        ans2.grid(column=1,row=a2)
        rad3.grid(column=0,row=a3)
        ans3.configure(text=quest[i].wrong2,bg="white")
        ans3.grid(column=1,row=a3)
        rad4.grid(column=0,row=a4)
        ans4.configure(text=quest[i].wrong3,bg="white")
        ans4.grid(column=1,row=a4)
    else:
        selected.set(None)
        a1=int(select[i][0])
        a2=int(select[i][1])
        a3=int(select[i][2])
        a4=int(select[i][3])
        rad1.grid(column=0,row=a1)
        ans1.configure(text=quest[i].ans,bg="white")
        ans1.grid(column=1,row=a1)
        rad2.grid(column=0,row=a2)
        ans2.configure(text=quest[i].wrong1,bg="white")
        ans2.grid(column=1,row=a2)
        rad3.grid(column=0,row=a3)
        ans3.configure(text=quest[i].wrong2,bg="white")
        ans3.grid(column=1,row=a3)
        rad4.grid(column=0,row=a4)
        ans4.configure(text=quest[i].wrong3,bg="white")
        ans4.grid(column=1,row=a4)


        
    return 

def clicked():
    global ans
    j=glo
    b=selected.get()
    if b!=None:
        selects[j]=b
        if b==1:
            ans[j]=1
        elif b>1 and b<5:
            ans[j]=0
    else:
        selects[j]=0
    return




def mark():
    result=messagebox.askyesno(title="Sumit confimation",message="Are you sur you want to Submit\nNote: The Exam will end on submitting ")
    if result:
        marks=0
        i=0
        for i in range (number):
            if ans[i]==0:
                marks-=wrong
            elif ans[i]==1:
                marks+=correct
        to=number*correct
        messagebox.showinfo(title="Test Submitted",message=("You have scored %d / %d"%(marks,to)))
        window.destroy()
    return


def nextq():
    i=glo+1
    setinfo(i)
    return

def prevq():
    i=glo-1
    setinfo(i)

    return

    
#The 'select question' Frame

frame2=Frame(window,height=900,width=300,bg="light yellow",bd=4,highlightbackground="grey",highlightthickness=2)
frame2.grid_propagate(0)




#the Question part
class mcq:
    def __init__(self,slno,q,ans,wrong1,wrong2,wrong3):
        self.slno=slno
        self.q=q
        self.ans=ans
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

    def display(self):
        print("\n\n\tQuestion ",self.slno," : ",self.q)
        print("\tAnswer : ",self.ans)
        print("\t Wrong : ",self.wrong1,"\n\t Wrong : ",self.wrong2,"\n\t Wrong : ",self.wrong3)


#Testing Phase questions

quest=list()

def backed():
    global number,correct,wrong,quest
    with open("Backup.csv",mode="r") as myfile:
        read=csv.reader(myfile)
        count=1
        for row in read:
            if count<=(number+1) and count!=1:
                quest[(int(row[0])-1)].slno=row[0]
                quest[(int(row[0])-1)].q=row[1]
                quest[(int(row[0])-1)].ans=row[2]
                quest[(int(row[0])-1)].wrong1=row[3]
                quest[(int(row[0])-1)].wrong2=row[4]
                quest[(int(row[0])-1)].wrong3=row[5]
            if count==1:
                number=int(row[0])
                correct=int(row[1])
                wrong=int(row[2])
                for i in range(number):
                    quest.append(mcq(0,"","","","",""))
            count+=1
    return
backed()

ans=[]
select=[]
qa=[]
for i in range(number):
    ans.append(2)
    select.append([0,0,0,0])
    selects.append(0)



#Creating the buttons
butt=list()
sl=0
def click(j):
    quest[j].display()
    setinfo(j)
    return

for i in range(number):
    butt.append(Button(frame2,text=(i+1),height=2,width=4,command=lambda j=i:click(j)))

label0=Label(frame2,height=2,bg="light yellow")   #this is the gap for the 'Questions' title to appear
label0.grid(row=0)
for i in range(number):
    c=i%5
    r=int(i/5)
    butt[i].grid(row=r+1,column=c,padx=8,pady=8)
    
    
Qlabel1=Label(frame2,text="Questions",bg="light yellow",font=("Arial",20),)
Qlabel1.place(x=80)



savebut=Button(frame1,text="Save",height=2,bg="green",fg="white",font=("Arial Bold",18),command=clicked)
savebut.place(x=1000,y=800)

fin=Button(frame2,text="Submit Test",height=2,bg="blue",fg="white",font=("Arial Bold",18),command=mark)
fin.place(x=75,y=800)

nextbut=Button(frame1,text="Next",height=2,bg="yellow",font=("Arial Bold",18),command=nextq)
nextbut.place(x=1100,y=800)

prevbut=Button(frame1,text="Previous",height=2,bg="yellow",font=("Arial Bold",18),command=prevq)
prevbut.place(x=850,y=800)


fir=Button(window,text="Start Exam",bg="light blue",command=waiting,height=3,)
fir.place(x=770,y=440)



window.mainloop()
