class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    @staticmethod
    def age_calculation(age):
        if age<17:
            print("you are in school")
        if age>18:
            print("Stop learning...... Start working")
# s1=Student("kawser",19240023)

print(Student.age_calculation(19))
 