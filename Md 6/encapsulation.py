class Bank:
    def __init__(self,holder_name,initail_name_deposit)->None:
        self.holder_name=holder_name # public attribute
        self._branch='banai' # Proated
        self.__balance=initail_name_deposit  # pivate attribute
    
    def depsit(self,amount):
        self.__balance+=amount
        return self.depsit
    def get_balance(self):
            return self.__balance
    
    def withdraw(self,amount): # encupcutaion 
        if amount<self.__balance :
            self.__balance=self.__balance-amount
            return amount
        else:
            return f'fokira taka ni {amount}'
            
    
      
rafsan=Bank('choto',10000)
 
print(rafsan.holder_name)
rafsan.depsit(40000)
rafsan.withdraw(500)
print(rafsan.get_balance())