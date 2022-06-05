# For Private class we can not access it outside of class nor it's subclass
class Parent:
    def __init__(self):
        self.__a=2 #hard coded xd
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self._a)

obj1=Child()