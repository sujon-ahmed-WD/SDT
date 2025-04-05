class Phone:
    name="samsung"
 # consturctor 
    def __init__(self,owner,brand,pries):
        self.owner=owner
        self.brand=brand
        self.pries=pries
my_phone=Phone('suj','iphone',20)
print(my_phone.owner,my_phone.brand,my_phone.pries)
my_fnd=Phone('kuj','mono kono',20)
print(my_phone.brand)
    