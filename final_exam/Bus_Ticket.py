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
class Admin:
  def __init__(self,username,password):
    self.username=username
    self.password=password
  
  def login(self,username,password):
    if(self.username==username)and(self.password==password):
      
      print("validate credentials")
      return True
    else:
      print(" Invalidate credentials")
      return False
class Passenger:
  def __init__(self,name,phone,bus):
     self.name=name
     self.phone=phone
     self.bus=bus

class BusSystem:
  buses_list=[]
  passengers_list =[]
  def  add_bus(self,number,route,total_seats,admin,username,password):
    
    if admin.login(username,password):
      newbus=Bus(number,route,total_seats)
      self.buses_list.append(newbus)
      print(f"new bus added{number}  {route} {total_seats}")
    else:
      print("You are not authorized to add a bus.")
  
       
    
  def book_ticket(self,book_bus_number, name, phone):
    self.name=name
    self.phone=phone
    for bus in self.buses_list:
     if bus.number==book_bus_number:
       if bus.available_seats()>0:
         bus.book_seat()
         newpassanger=Passenger(name,phone,bus)
         self.passengers_list.append(newpassanger)
        
       else:
         print("no seat available")
       return
    print("no bus available")
  
  def  show_buses(self):
       for bus in self.buses_list:
         print(f"Bus Number: {bus.number}, Route: {bus.route}, Available Seats: {bus.available_seats()}")
       
         
         


  
admin = Admin("admin", "1234")
system = BusSystem()

while True:
    print("\nUser Menu:\n1. Admin Login\n2. Book Ticket\n3. View Buses\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter Admin username: ")
        password = input("Enter Admin password: ")
        if admin.login(username, password):
            while True:
                print("\nAdmin Menu:\n1. Add Bus\n2. View All Buses\n3. Logout")
                admin_choice = int(input("Enter your choice: "))
                if admin_choice == 1:
                    number = int(input("Enter bus number: "))
                    route = input("Enter route: ")
                    total_seats = int(input("Enter total seats: "))
                    system.add_bus(number, route, total_seats, admin, username, password)
                elif admin_choice == 2:
                    system.show_buses()
                elif admin_choice == 3:
                    print("Admin logged out.")
                    break
                else:
                    print("Invalid choice. Try again.")
        else:
            print("Invalid credentials. Access denied.")

    elif choice == 2:
        bus_number = int(input("Enter bus number: "))
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        system.book_ticket(bus_number, name, phone)
        print("Ticket booked successfully. Fare: ৳500")

    elif choice == 3:
        system.show_buses()

    elif choice == 4:
        print("Exiting system. Thank you!")
        break

    else:
        print("Invalid choice. Try again.")

 