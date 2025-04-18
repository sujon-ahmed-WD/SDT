# Coustomer
# Employee
# Admin

from abc import ABC


# step 1
class USER(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


# this is a Emplye
class Employee(USER):
    def __init__(self, name, phone, email, address, age, designarion, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designaetion = designarion
        self.salary = salary

class Admin(USER):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_Employee(self, Restaurent, employee):
        Restaurent.add_Employee(employee)

    def viwe_Employee(self, Restaurent):
        Restaurent.viwe_Employee()
        
    def add_manu_item(self,Restaurent,item):
        Restaurent.manu.add_manu_items(item)    
    def remove_item(self,Restaurent,item):
        Restaurent.manu.remove_manu_item(item)

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employee_list = []  # ata holo database
        self. menu=Food_item()

    def add_Employee(self, employee):
        self.employee_list.append(employee)

    def viwe_Employee(self):
        print("this is employee list !!!")
        for emp in self.employee_list:
            print(f"{emp.name} {emp.phone} {emp.email} {emp.address} {emp.age}")

class Manue:
    def __init__(self):
        self.items = []

    def add_manu_items(self, item):
        self.items.append(item)

    def find_manu_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.name.lower():
                return item_name
        return None

    def remove_manu_item(self, item_name):
        item = self.item(item_name)
        if item:
            self.items.remove(item)
            print("item Deleted")
        else:
            print("item Not found ! ! !")
    
    def shwo_manu_item(self):
        print("******Manu*******")
        print("Name\tprice\tquantity")
        for item in self.items:
            print(f"{item.name}    {item.pries}      {item.quntaity}")


class Food_item:
     def __init__(self,name,pries,quntaity):
         self.name=name
         self.pries=pries
         self.quntaity=quntaity
         

# ad = Admin("admin", 43, "ad@gmaill.com", "Dhaka")
# ad.addEmployee("sujon", 294389043, "suj@gmail.com", "Dhaka", 18, "chef", 20)

# ad.viwe_Employee()
mn=Manue()
item=Food_item("Pizza",800,10)
mn.add_manu_items(item)
mn.shwo_manu_item()
