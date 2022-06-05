
class Grandpa:
    def showG(self):
        print("I am From Grandpa Class")

class Father:
    def showF(self):
        print("I am From Father Class")

class Child(Father,Grandpa):
    def showC(self):
        print("I am From child class")

person=Child()
print(isinstance(person,Child))
print(isinstance(person,Father))
print(isinstance(person,Grandpa))

# From the execution we can see that person is a object of every class..So we can access them 

person.showC()
person.showF()
person.showG()

'''
what will happen if i have constructor ???
'''

print(Child.__mro__)