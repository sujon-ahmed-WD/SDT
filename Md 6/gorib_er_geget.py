class Laptop:
    def __init__(self,brand,price,color,memory)->None:
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        return f'running laptop{self.brand}'
    def coding(self):
        return f'learing in python in Praticinge '
class Phone:
    def __init__(self,brand,price,color,memory,dual_sim)->None:
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
        self.dual_sim=dual_sim
    def run(self):
        return f'phone tipa tipe kories nh'
    def phone_call(self,number,text):
        return f'Sending SMS to {number} with {text}'
class Camera:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
    def run(self):
        pass
    def change_lans(self):
        pass
    
        