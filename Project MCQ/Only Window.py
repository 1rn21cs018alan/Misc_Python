from tkinter.ttk import *
from tkinter import *


window=Tk()
window.title("MCQ Exam")
window.attributes('-fullscreen',True)
window.geometry("1600x900+0+0")

selects=list()
class Opt():
    global selects
    selects.append(IntVar())        
    rad1=Radiobutton(frame1,value=1,variable=selects[len(selects)-1],command=(lambda a=len(selects):mark(a)))
    rad2=Radiobutton(frame1,value=2,variable=selects[len(selects)-1],command=(lambda a=len(selects):mark(a)))
    rad3=Radiobutton(frame1,value=3,variable=selects[len(selects)-1],command=(lambda a=len(selects):mark(a)))
    rad4=Radiobutton(frame1,value=4,variable=selects[len(selects)-1],command=(lambda a=len(selects):mark(a)))
    ans1=Label(frame1,bg="white")
    ans2=Label(frame1,bg="white")
    ans3=Label(frame1,bg="white")
    ans4=Label(frame1,bg="white")
    scatter=[2,3,4,5]
    def __init__(self,ans,w1,w2,w3):
        self.ans1.configure(text=ans)
        self.ans2.configure(text=w1)
        self.ans3.configure(text=w2)
        self.ans4.configure(text=w3)
        random.shuffle(self.scatter)
    def show(self):
        
        self.rad1.grid(row=self.scatter[0],column=0)
        self.rad2.grid(row=self.scatter[1],column=0)
        self.rad3.grid(row=self.scatter[2],column=0)
        self.rad4.grid(row=self.scatter[3],column=0)
        
        self.ans1.grid(row=self.scatter[0],column=1)
        self.ans2.grid(row=self.scatter[1],column=1)
        self.ans3.grid(row=self.scatter[2],column=1)
        self.ans4.grid(row=self.scatter[3],column=1)

    def hide()
        self.rad1.grid_forget()
        self.rad2.grid_forget()
        self.rad3.grid_forget()
        self.rad4.grid_forget()
        
        self.ans1.grid_forget()
        self.ans2.grid_forget()
        self.ans3.grid_forget()
        self.ans4.grid_forget()
    
def showwin(): # to show the frames
    frame1.grid(row=0,column=0)
    frame2.grid(row=0,column=1)
    fir.destroy()
    makebut()
    return

#The Frames
def makef1():
    frame1=Frame(window,height=900,width=1300,bg="white",bd=4,highlightbackground="grey",highlightthickness=2)
    frame1.grid_propagate(0)
    frame1.grid(row=0,column=0)
    return frame1



def makef2():
    frame2=Frame(window,height=900,width=300,bg="light yellow",bd=4,highlightbackground="grey",highlightthickness=2)
    frame2.grid_propagate(0)
    frame2.grid(row=0,column=1)
    return frame2


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

number=int(input("Enter number : "))

quest=list()
for i in range(number):
    a=i+1
    quest.append(mcq((a),("QA-%d"%a),("Ans-%d"%a),("Wrong 1:%d"%a),("Wrong 2:%d"%a),("Wrong 3:%d"%a)))
    




#Creating the buttons
butt=[]
def click(ind):
    quest[i].display()

def makebut():
    global butt
    for i in range(number):
        butt.append(Button(frame2,text=(i+1),height=2,width=4,command=click(i)))

    label0=Label(frame2,height=2,bg="light yellow")   #this is the gap for the 'Questions' title to appear
    label0.grid(row=0)
    for i in range(number):
        c=i%5
        r=int(i/5)
        butt[i].grid(row=r+1,column=c,padx=8,pady=8)
    
    
    Qlabel1=Label(frame2,text="Questions",bg="light yellow",font=("Arial",20),)
    Qlabel1.place(x=80)



frame1=makef1()
frame2=makef2()
fir=Button(window,text="Start",command=showwin)
fir.grid(row=0,column=0)



window.mainloop()
