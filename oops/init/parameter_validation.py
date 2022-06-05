class item:
    def __init__(self,name:str,price:int,quantity=0):
        assert price>=0,f"price {price} can not be less then zero!"
        assert quantity>=0,f"quantity {quantity} can not be less then zero!"

        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        print(self.price*self.quantity)

item1=item("phone",3000,-1)
item1.total_price()