class Person:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person): #Inheriting person class . now Employee is a childclass of a person class.Employee class have all of the attribute which have person class.We can check it with __base__
    def isEmployee(self):
        return True

print("Employee class is a child of ",Employee.__base__)
emp=Person("Kawser")
print(emp.get_name(),emp.isEmployee())

emp=Employee("kamrul")
print(emp.get_name(),emp.isEmployee())

