# protected is a member which allows you to access it within the class and the subclasses. it's invention is single _
class Parent:
    def __init__(self):
        self._a=2 #hard coded xd
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self._a)
         

        self._a=5
        print(self._a)
obj1=Child()
