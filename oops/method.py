class item:
    def total_price(self,x,y):
        print(x*y)
item1=item()
item1.name="phone"
item1.price=3000
item1.quantity=5
item1.total_price(item1.price,item1.quantity)

item2=item()
item2.name="laptop"
item2.price=30000
item2.quantity=3
item2.total_price(item2.price,item2.quantity)