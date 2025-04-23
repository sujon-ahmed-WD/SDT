
from abc import ABC ,abstractmethod
class Food_Item(ABC):
    def __init__(self,name,price):
        self.__name=name
        self.__price=price
        
    def get_price(self):
        return self.__price
    
    def get_name(self):
        return self.__name
    
    @abstractmethod
    def prepare(self):
        pass
    

class Restrurant_Owener:
    orderlist=[]
    
    def add_orders(self,order):
        self.orderlist.append(order)
class Burger(Food_Item):
    def __init__(self):
        super().__init__("Burger", 150)
    def prepare(self):
        print( "Grilling the burger patty and adding sauce ... ")
        
    def __repr__(self):
        return self.get_name()

class Pizza(Food_Item):
    def __init__(self):
        super().__init__("SPacye PIzza", 550)
        
    def prepare(self):
        print( "Pizza boro ta deo dada  the burger patty and adding sauce ... ")
    
    def __repr__(self):
        return self.get_name()

class Drink(Food_Item):
    def __init__(self):
        super().__init__("Lemon_jus", 250)
        
    def prepare(self):
        print( "mojo boro ta deo dada  the burger patty and adding sauce ... ")
        
    def __repr__(self):
        return self.get_name()

class Order:
    #self.items=[]                         ata dela sob aki       jaga thka add hoba   ..........
    def __init__(self):
        self.items=[]
    
    def add_item(self,food_item):
        self.items.append(food_item)
        
    def process_order(self):
        print("\n Prepraing your item")
        for item in self.items:
            item.prepare()
    
    def show_order(self):
        print("\n Your Order Summery ")
        total=0
        
        for item in self.items:
            print(f"-{item} - {item.get_price()}")
            total+=item.get_price()
        print(f"Total Price :{total} BDT ")
    
    def __repr__(self):
        items_name=" " 
        for item in self.items:
            items_name+=f"{item.get_name()}, "
        return items_name
        
        
Burger=Burger()
Pizza=Pizza()
drink=Drink()
order=Order()
order.add_item(Burger)
order.add_item(Pizza)
 

owner=Restrurant_Owener()
owner.add_orders(order) 
print(order.items)
  
# x_order=Order()
# #COUSTOMER
# x_order.add_item(Burger)
# x_order.add_item(Pizza)
 
# Proces
# x_order.process_order()
# x_order.show_order()

