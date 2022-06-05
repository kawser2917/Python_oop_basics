# polymorphism with inheritance

class Bird:
    def Intro(self):
        print("There are different types of birds")
    def flight(self):
        print("some can fly and some can not")

class Parrot(Bird):
    def flight(self):
        print("parrot can fly")

class Penguian(Bird):
    def flight(self):
        print("Penguian can not fly")

b=Bird()
b.Intro()
b.flight()

p=Parrot()
p.Intro()
p.flight()

pn=Penguian()
pn.Intro()
pn.flight()
