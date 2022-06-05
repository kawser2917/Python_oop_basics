#we need classmethod for doing some work for with class.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name+" "+"got" +" "+ str(self.marks),"%")
    
    @classmethod
    def avg_marks(cls,name,mark):
        print (name,str((int(mark)/600)*100)+"%")

s1=Student("kawser",80)
name="kaharul"
total_marks=560

Student.avg_marks("kaharul",560)
 

