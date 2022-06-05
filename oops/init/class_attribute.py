class Item:
    # i can access the pay rate from class label and instance label
    pay_rate=0.8

    def __init__(self,name:str,price:int,quanity=0):
        self.name=name
        self.price=price
        self.quantity=quanity
    def applying_discount(self):
        self.price = self.price*self.pay_rate #if we access with item.pay_rate then it will be always 0.8 i can't change it from instance label

item1=Item("phone",3000,5)
item1.applying_discount()
item2=Item("laptop",50000,4)
item2.pay_rate=0.7 #now for item2 pay_rate will be 30 percent
item2.applying_discount()

# __dict__: this keyword will show me how much thing i have into the class label and instance label
print(Item.__dict__)
print(item1.__dict__)

print(item1.price)
print(item2.price)
 
