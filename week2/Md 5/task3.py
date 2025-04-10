class Atendance:
    
    def __init__(self,atendance):
        self.atendance=atendance
        self.marks=40
        
    def get_mark(self):
        return self.marks
    
    def aten(self,atendance):
        if atendance=="yes":
            print("vety good")
        
    def mark(self,marks):
        if marks>20:
            print(f'now it us your res {self.get_mark()}')   
me=Atendance("sujon")
me.aten('yes')
me.mark(25)