# MCQ Test program

from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

class mcq():

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


number=0  #Total questions
correct=0  #Marks per correct question
wrong=0  #Marks lost per wrong question
Totalmarks=0

quest=list()

def backup():
    with open("Backup.csv",mode="w") as myfile:
        qb=[]
        qc=[]
        qc.append(number)
        qc.append(correct)
        qc.append(wrong)
        qb.append(qc)
        writer=csv.writer(myfile,lineterminator="\n")
        for i in range(number):
            qa=[]
            qa.append(quest[i].slno)
            qa.append(quest[i].q)
            qa.append(quest[i].ans)
            qa.append(quest[i].wrong1)
            qa.append(quest[i].wrong2)
            qa.append(quest[i].wrong3)
            qb.append(qa)
        writer.writerows(qb)
    return

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


def teacher():   #try to make this a window after normal execution
    global number,correct,wrong,Totalmarks
    number=int(input("\tTotal Number of Questions in the exam : "))
    correct=int(input("\tMarks Gained per correct in the exam : "))
    wrong=int(input("\tMarks Lost per wrong questions in the exam : -"))
    Totalmarks=number*correct
    i=1
    for i in range (number):
        slno=i+1
        print("\n\n\n\t\tQuestion ",slno)
        q=input("\tEnter Question : ")
        ans=input("\tEnter Correct Answer : ")
        wrong1=input("\tEnter first wrong Answer : ")
        wrong2=input("\tEnter second wrong Answer : ")
        wrong3=input("\tEnter third wrong Answer : ")
        quest.append(mcq(slno,q,ans,wrong1,wrong2,wrong3))
        i+=1
    #print("Enter blank(1) to start the test")
    backup()
    return
def show():
    def click():
        print("Click")
    for i in range(number):
        quest[i].display()
        click()
    return

def blank(a):
    for i in range(2):
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if a==1:
        input("\tPress enter to start the test")
        print("\t\tStarting Test.........")
        time.sleep(1)
        test()
    return

def test():
    
    mark=0
    print("\tPlease wait for the test to load")
    time.sleep(4)
    print("\tLoading complete")
    time.sleep(1.5)
    blank(0)
    print("\tNote: This is an MCQ type exam and you must only enter the option number of your answer\n")
    print("\t Number of questions : ",number,"\n\t Marks for correct answer : ",correct,"\n\t Marks for wrong answer : -",wrong,"\n\t Total Marks : ",Totalmarks)
    for i in range(number):
        print("\n\n\tQuestion ",quest[i].slno," : ",quest[i].q,"\n")
        a=random.choice([1,2,3,4])
        b=1
        if a==1:
            print("\tOption ",a," : ",quest[i].ans)
            b+=1
        print("\tOption ",b," : ",quest[i].wrong1)
        b+=1

        if a==2:
            print("\tOption ",a," : ",quest[i].ans)
            b+=1
        print("\tOption ",b," : ",quest[i].wrong2)
        b+=1

        if a==3:
            print("\tOption ",a," : ",quest[i].ans)
            b+=1
        print("\tOption ",b," : ",quest[i].wrong3)

        if a==4:
            print("\tOption ",a," : ",quest[i].ans)
        print("\tOption  5 :  Skip Question")
        while True:
            opt=int(input("\n\tEnter Option Number : "))
            if opt==a:
                mark+=correct
                break
            elif opt!=5:
                mark-=wrong
                break
            elif opt<1 or opt>5:
                print("\tOption Does Not Exist, Please Reenter Your Option\n")
                break
    print("\n\n\t\tAll Answers Have been Submitted")
    time.sleep(1.5)
    print("\n\n\t\tYou Have scored : ",mark,'/',Totalmarks)
    time.sleep(2)
    cho=input("Enter Y to Restart Test or N to Exit : ")
    cho.lower()
    if cho=="y":
        blank(1)
    return

print("\n\n\t\tExaminer, Please Create the Exam Questions\n\n\n")

yon=input("\n\t\tEnter 'W' to Write a New Exam or 'I' to Import test from Backup.csv : ")
yon.lower()
if yon=="w":
    teacher()
else:
    backed()
    
blank(1)
