 
class Item:
    all=[]
    def __init__(self,name:str,price:int,quantity=0):
        assert price>=0,f"price {price} can not be less then zero!"
        assert quantity>=0,f"quantity {quantity} can not be less then zero!"

        self.name=name
        self.price=price
        self.quantity=quantity

        Item.all.append(self)
    def total_price(self):
        print(self.price*self.quantity)
    def __repr__(self):
        return f"({self.name},{self.price},{self.quantity})"

item1=Item("Phone",3000,3)
item2=Item("laptop",2000,5)
item3=Item("cable",20,5)
item4=Item("mouse",50,100)

# if we don't use __repr__ method then this print line will show us memory address of the instances
print(Item.all)


# from that we can see that we can keep all of the instances into our list so that we can use it when we need the item for working
for instance in Item.all:
    print(instance.name)