class Bank:
    def __init__(self,balacne):
        self.balacne=balacne
        self.min_withdrow=100
        self.max_withdrow=10000
    
    def get_balance(self):
        return self.balacne
    
    def deposite(self,amount):
        if amount>0:
            self.balacne+=amount
     
    def withdrow(self,amount):
        if amount<self.min_withdrow:
            print("kom taka dai nh bro ")
        elif amount>self.max_withdrow:
            print("ato taka ni bank bro")
        else:
            self.balacne-=amount
            print(f'hear is amonunt money {amount}')
            print(f'tomer botoman taka asa akhono: {self.get_balance()}')
            
            
brack=Bank(150000)
brack.withdrow(25)
# print(brack.balacne)
brack.withdrow(2500000)
brack.withdrow(1500)
