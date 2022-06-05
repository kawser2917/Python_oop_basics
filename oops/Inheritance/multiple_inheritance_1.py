# Multiple inheritance with constructor

class Grandpa:
    def __init__(self):
        print("I am grandpa Constructor")
    def showG(self):
        print("I am From Grandpa Class")

class Father:
    def __init__(self):
        super().__init__()
        print("I am Father Constructor")
    def showF(self):
        print("I am From Father Class")

class Child(Father,Grandpa):
    def __init__(self):
        super().__init__()
        print("I am child Constructor")
    def showC(self):
        print("I am From child class")

person=Child()

 