class Person:
    def __init__(self,name,age,h,w):
        self.name=name
        self.age=age
        self.h=h
        self.w=w
    def eat(self):
        print("give me a anaros")
    
class Student(Person):
    def __init__(self, name, age, h, w):
        super().__init__(name, age, h, w)
    
                                                                                              
    def eat(self):
        print("Vagitabls")
    def must(self):
        raise ImportError

class shobo(Student):

    def __init__(self, name, age, h, w,team):
        self.team=team
        super().__init__(name, age, h, w)
    
   
    def eat(self): # override method
        print("multi")
    def must(self):
        print("hello")
    
    # + sign oprator method over load
    def __add__(self,other):
        return self.age+ other.age
    # - sign oprator method   
    def __mul__(self,other):
        return self.age*other.age
        
sujon=shobo('sujon',19,5,55,'BD')
mujon=shobo('mujon',20,8,40,'BD')

print(sujon+mujon)
print(sujon*mujon)

