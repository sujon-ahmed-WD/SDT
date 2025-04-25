from abc import ABC, abstractmethod


class Restrurant_Owener:
    orderlist = []

    def add_orders(self, order):
        self.orderlist.append(order)
owner = Restrurant_Owener()


class Customer:
   def __init__(self,name):
       self.name=name





class Food_Item(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    @abstractmethod
    def prepare(self):
        pass


class Burger(Food_Item):
    def __init__(self):
        super().__init__("Burger", 150)

    def prepare(self):
        print("Grilling the burger patty and adding sauce ... ")

    def __repr__(self):
        return self.get_name()


class Pizza(Food_Item):
    def __init__(self):
        super().__init__("SPacye PIzza", 550)

    def prepare(self):
        print("Pizza boro ta deo dada  the burger patty and adding sauce ... ")

    def __repr__(self):
        return self.get_name()


class Drink(Food_Item):
    def __init__(self):
        super().__init__("Lemon_jus", 250)

    def prepare(self):
        print("mojo boro ta deo dada  the burger patty and adding sauce ... ")

    def __repr__(self):
        return self.get_name()


class Order:
    # self.items=[]                         ata dela sob aki       jaga thka add hoba   ..........
    def __init__(self):
        self.items = [] # instance attribute 
        owner.add_orders(self)

    def add_item(self, food_item):
        self.items.append(food_item)

    def process_order(self):
        print("\n Prepraing your item")
        for item in self.items:
            item.prepare()

    def show_order(self):
        print("\n Your Order Summery ")
        total = 0

        for item in self.items:
            print(f"-{item} - {item.get_price()}")
            total += item.get_price()
        print(f"Total Price :{total} BDT ")

    def __repr__(self):
        items_name = " "
        for item in self.items:
            items_name += f"{item.get_name()}, "
        return f"[{items_name}]"


# Burger=Burger()
# Pizza=Pizza()
# drink=Drink()
# x_order=Order()
# x_order.add_item(Burger)
# x_order.add_item(Pizza)


# owner=Restrurant_Owener()
# owner.add_orders(self)

# y order
# y_order=Order()
# y_order.add_item(drink)
# print(owner.orderlist)


# x_order=Order()
# #COUSTOMER
# x_order.add_item(Burger)
# x_order.add_item(Pizza)

# Proces
# x_order.process_order()
# x_order.show_order()

# --------------------------- Republic Section--------------

burger = Burger()
pizza = Pizza()
drink = Drink()
order=Order()
while True:

    print("Choose an Option\n" "1.Owner\n" "2.Customer\n")
    opstion = int(input("Your selection : "))

    if opstion == 1:
        """Owner"""
        print("Select an option\n" "1.Process Order\n" "2.Show Order")
        owner_selection=int(input("Your Selection :"))
        
         # Practice Task
          #Order list iterate process order, #show order
        if owner_selection==1:
             order.process_order()
        elif owner_selection==2:
            order.show_order()

        
    elif opstion == 2:
        """Customer"""
        name=input("Enter Your name  :  ")
        customer=Customer(name)
        
        menu_list=[burger,pizza,drink]
        
        while True:
            print("Select an option\n"
                  "1.Show Menu\n"
                  "2.Add Item\n"
                  "3.Exit")
            
            customer_selection=int(input("Your Selection : "))
            if customer_selection==1:
                for i in range(len(menu_list)):
                    print(f"{i} {menu_list[i]}")
    
            elif customer_selection==2:
                order_input=int(input("Enter item code: "))
                print(menu_list[order_input])
                order.add_item(menu_list[order_input])
                print("order is addedd")
            elif customer_selection==3:
                break
            else:
                print("Wrong input.Try Agin!!")
