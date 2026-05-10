# Python project-student marks data analyser
# project by Tharun.P & Hemanth.P


import matplotlib.pyplot as plt
import numpy as np

class Student_data:

    def __init__(self,name,prn):
        self.name=name
        self.prn=prn

    def Linear_data(self):
        n=int(input("enter number of subjects"))
        marks=[0]*n
        subjects=[0]*n
        for i in range(len(marks)):
            subjects[i]=input("enter subject")
            marks[i]=int(input("enter marks"))
        subjects=np.array(subjects)
        marks=np.array(marks)
        dict={"marker":".","markersize":"5","markerfacecolor":"cyan"}
        plt.xlabel("Subjetcs",color="magenta")
        plt.ylabel("Marks",color="orange")
        plt.title("Student Marks Analaysis",color="aqua")
        plt.plot(subjects,marks,**dict)
        plt.show()

    def Bar_data(self):
        n=int(input("enter number of subjects"))
        marks=[0]*n
        subjects=[0]*n
        for i in range(len(marks)):
            subjects[i]=input("enter subject")
            marks[i]=int(input("enter marks"))
        subjects=np.array(subjects)
        marks=np.array(marks)
        plt.bar(subjects,marks,color="skyblue")
        plt.xlabel("Subjects",color="orange")
        plt.ylabel("Marks",color="red")
        plt.title("Student Marks Analaysis",fontsize=15,color="pink")
        plt.show()
    
    def Pie_chart(self):
        n=int(input("enter number of subjects"))
        marks=[0]*n
        subjects=[0]*n
        for i in range(len(marks)):
            subjects[i]=input("enter subject")
            marks[i]=int(input("enter marks"))
        plt.pie(marks, labels=subjects, autopct="%1.1f%%")
        plt.title("Student Marks Analaysis",color="pink")
        plt.show()

    def scatter(self):
        n=int(input("enter number of subjects"))
        marks=[0]*n
        subjects=[0]*n
        for i in range(len(marks)):
            subjects[i]=input("enter subject")
            marks[i]=int(input("enter marks"))
        subjects=np.array(subjects)
        marks=np.array(marks)
        plt.scatter(subjects,marks)
        plt.title("Student Marks Analaysis",color="pink")
        plt.xlabel("Subjects",color="orange")
        plt.ylabel("Marks",color="red")
        plt.show()


s1=Student_data("kumar",2009)
s1.Bar_data()
