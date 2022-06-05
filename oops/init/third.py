


class item:

    # we can give specific data type for parameter. so that no one can keep another type of value to it's parameter
    # i have said
    
    # name will accept only str type of value
    # price will accept float type of value
    # if we give default value then we do not need to say specific value type
    def __init__(self, name: str, price: float, quantity=0):
        self.name=name
        self.price=price
        self.quantity=quantity
    def total_price(self):
        print(self.price*self.quantity)

item1=item("phone",3000,3)
item2=item("laptop",4002,30)


item1.total_price()
item2.total_price()