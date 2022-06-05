class item:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
# In the previous function we needed to create instances and assign value. if we use init method we don't need to create assign value by it's corresponding value. we can easily assign it by passing argument

item1=item("phone",3000,4)
item2=item("laptop",30000,5)
print(item1.name)
print(item2.name)