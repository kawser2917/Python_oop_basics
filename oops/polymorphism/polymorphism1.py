# polymorphism is used for same function with different function
# here is the example of the polymorphism with obj

class Tomato:
    def type(self):
        print("Vegetables")
    def color(self):
        print("red")

class Apple:
    def type(self):
        print("Fruit")
    def color(self):
        print("Red")
def display(obj):
    obj.type()
    obj.color()
T1=Tomato()
A1=Apple()

display(T1)
display(A1)