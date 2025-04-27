class Bus:
    def __init__(self,number,route,total_seats):
        self.number=number
        self.route=route
        self.total_seats=total_seats
        self.booked_seat=0
    
    def available_seats(self):
      unbooked_seat=self.total_seats-self.booked_seat
      return unbooked_seat

    def book_seat(self):
       if self.available_seats()>0:
         self.booked_seat+=1
       else:
         print("No seat available.")
class Passenger:
  def __init__(self,name,phone,bus):
     self.name=name
     self.phone=phone
     self.bus=bus

class BusSystem:
  def __init__(self):
    self.buses_list=[]
    self.passengers_list =[]   
  
  def add_buss_list(self):
    pass
  def add_passengers_list(self):
    pass
 

 

 