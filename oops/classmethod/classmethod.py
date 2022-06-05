import csv

class Item:
    all=[]
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
        Item.all.append(self)
    def __repr__(self):
        return f"({self.name},{self.price},{self.quantity})"
        
    @classmethod
    def initiative_from_csv(self):
        with open("items.csv","r") as f:
            reader=csv.DictReader(f)
            items=list(reader)
        for item in items:
            # This below line will show everything which we have in the csv
            # print(item)
            # for making the csv item to our class item we need to follow like this.
            Item(
               name=item.get("name"),
               price=int(item.get("price")),
               quantity=int(item.get("quantity"))
           )

    
# this below line work if we print the item. this calling show us our output 
# Item.initiative_from_csv()
print(Item.all)
        