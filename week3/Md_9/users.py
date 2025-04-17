#Coustomer
#Employee
#Admin

from abc import ABC

# step 1
class USER(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
    
# this is a Emplye
class Employee(USER):
        def __init__(self,name,phone,email,address,age,designarion,salary):
            super().__init__(name,phone,email,address)
            self.age=age
            self.designaetion=designarion
            self.salary=salary
# emp=Employee("sujon",294389043,"suj@gmail.com","Dhaka",18 ,"chef",20)
# print(emp.name)


class Admin(USER):
    def __init__(self, name, phone, email, address):
          super().__init__(name, phone, email, address)
          
    def add_Employee(self,Restaurent,employee):
            Restaurent.add_Employee(employee)
    
    
    def viwe_Employee(self,Restaurent):
        Restaurent.viwe_Employee()
        
    
    
class Restaurent:
    def __init__(self,name):
        self.name=name
        self.employee_list=[] # ata holo database 
        
    def add_Employee(self,employee):
        self.employee_list.append(employee)
        #print(f"{name} is added! !")
              
        # Employe class jono akta object toiri kora holo ...........
        #employee=Employee(name,phone,email,address,age,designarion,salary) # akna kno self use holo nh
    def viwe_Employee(self):    
        print("this is employee list !!!")
        for emp in self.employee_list:
            print(f"{emp.name} {emp.phone} {emp.email} {emp.address} {emp.age}")
    
    
    
    
ad=Admin("admin",43,"ad@gmaill.com","Dhaka")
ad.addEmployee("sujon",294389043,"suj@gmail.com","Dhaka",18 ,"chef",20)

ad.viwe_Employee()