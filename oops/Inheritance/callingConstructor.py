class Person:
    def __init__(self,name,idNumber):
        self.name=name
        self.idNumber=idNumber
    def display(self):
        print(self.name)
        print(self.idNumber)
class Employee(Person):
    '''
    # if we do like this then we can not access the constructor of parent class. the parent's class constructor will be unavialable to the child class. 
    def __init__(self,salary,post):
        self.salary=salary
        self.post=post
    '''
    # For solving this problem we have to write the parents constructor in the child constructor.
    def __init__(self,name,idNumber,salary,post): #now we have all of the instance variable 
        self.name=name
        self.idNumber=idNumber
        self.salary=salary
        self.post=post
        # Note: boring code.. i need to repeat my code  again .. it's bad practice for inheritance 

emp=Employee("kawser",102030,500000,"Associate Engineer")
emp.display()

'''
for fixing the repeating code we need to use super calls 
'''