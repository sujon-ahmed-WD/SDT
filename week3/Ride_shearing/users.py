from abc import ABC,abstractmethod

class USER(ABC):
    def __init__(self,name,email,nid):
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=0
        
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
class Rider(USER):
    def __init__(self, name, email, nid,current_location,initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet=initial_amount
        self.current_location=current_location

    def display_profile(self):
        print(f"{self.name} and email {self.email}")
    
    def loead_cash(self,amount):
        if amount>0:
            self.wallet+=amount
        else:
            print("Amount Less then 0")
    
    def update_location(self,current_location):
        current_location=current_location
    
    def request_ride(self,ride_shearing,destination):
        pass
    def show_current_ride(self):
        print(self.current_ride)