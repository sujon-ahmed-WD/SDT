class Shop:
    
    def __init__(self,byer):
        self.byer=byer
        self.cart=[] # cart is instace attrubute
        
    def add_to_cart(self,item):
        self.cart.append(item)

suj=Shop('sd')
suj.add_to_cart('juta')
suj.add_to_cart('pan')

jon=Shop('jon')
jon.add_to_cart('ganji')
jon.add_to_cart('shart')

print(suj.cart)
print(jon.cart)
 
  