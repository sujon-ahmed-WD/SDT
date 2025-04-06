class Shop:
    cart=[] # This is  Class attribute
    def __init__(self,byer):
        self.byer=byer
    def add_to_cart(self,item):
        self.cart.append(item)
suj=Shop('keb')
suj.add_to_cart('show')
suj.add_to_cart('shwoos')
print(suj.cart)
    
    