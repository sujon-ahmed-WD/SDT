# base class, parent class, common attribute + functionality class
# derived class, child class, uncommon attribute + functionality class
class Gadget:
    
    def __init__(self,brand,price,color,orign):
        self.brand=brand
        self.price=price
        self.color=color  
        self.orign=orign
    def run(self):
        return f'Running Laptop: {self.brand}'
    
class Laptop:
     def __init__(self,memory,ssd)->None:
    
        self.memory=memory
        self.ssd=ssd
     
     def coding(self):
        return f'learing in python in Praticinge '
class Phone(Gadget):
    def __init__(self,brand,price,color,orign,dual_sim,memory)->None:
     
        self.memory=memory
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,orign)
        
    def __repr__(self):
        return f'{self.brand},{self.price},{self.color},{self.orign}'
     
    def phone_call(self,number,text):
        return f'Sending SMS to {number} with {text}'
    
class Camera:
    def __init__(self,pixel):
 
        self.pixel=pixel
 
    def change_lans(self):
        pass
    
# inheritence
myphone=Phone('iphone',12000,'silver','chini','banlalink',True)
#my_phone_phone_call()
print(myphone.brand)
print(myphone)
