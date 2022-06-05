# Another way to inherit constructor for multiple inheritance
class Grandpa:
    def __init__(self):
        print("I am grandpa Constructor")
    def showG(self):
        print("I am From Grandpa Class")

class Father:
    def __init__(self):
       
        print("I am Father Constructor")
    def showF(self):
        print("I am From Father Class")

class Child(Father,Grandpa):
    def __init__(self):
        Grandpa.__init__(self) #we can do this for accessing intances
        Father.__init__(self)
        print("I am child Constructor")
        
    def showC(self):
        print("I am From child class")

person=Child()