class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart= []
    def add_to_chart(self,item,price,quntity):
        product={'item':item, 'price':price,'quntity':quntity}
        self.cart.append(product)
    
    def chak_out(self,amount):
        total=0
        for item in  self.cart:
            total+=item ['price'] *  item['quntity']
        print('total price',total)
        if amount<total:
            print(f'aro keso taka lagbo {total-amount}')
        else:
            print(f'ato taka paban amier kasa apni {amount-total}')
swapn=Shopping('ali bhi')
swapn.add_to_chart('alu',50,5)
swapn.add_to_chart('ata',60,5)
swapn.add_to_chart('oil',90,5)

print(swapn.cart)
swapn.chak_out(1200)