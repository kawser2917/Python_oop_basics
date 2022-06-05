# abstraction is used for hiding some functionality from user
# suppose in our home we have tv and remote. if we press in + then the volume will increase we know the volume will increase but we don't know how it increased

from abc import ABC,abstractmethod
class Car:
    @abstractmethod
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("tesla mileage is 30km")
class Suzuki(Car):
    def mileage(self):
        print("suzuki mileage is 25km")

c=Car()
T=Tesla()
S=Suzuki()

c.mileage()
T.mileage()
S.mileage()
