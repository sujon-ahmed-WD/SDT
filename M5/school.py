class Student:
    def __init__(self,name,current_class,id):
        self.name=name
        self.id=id
        self.currnt_class=current_class
    
    def __repr__(self)->str:
        return f'Studant:{self.name},id:{self.currnt_class},id{self.id}'
        
    
class Techer:
        def __init__(self,name,id,sub)->None:
            self.name=name
            self.subject=sub
            self.id=id
        def __repr__(self):
            return f'Techer :{self.name},subject:{self.subject},id:{self.id}'

class School:
    def __init__(self,name)->None:
         self.name=name
         self.teachers=[]
         self.students=[]
    def add_techer(self,name,subject):
        id=len(self.teachers)+101
        teacher=Techer(name,subject,id)
        self.teachers.append(teacher)
   
    def __repr__(self)->str:
         print("welcome to",self.name)
         print('------------OUR TECHER----------')
         for techer in self.teachers:
             print(techer)
         print('-------------OUR STUDENT---------')
         for studnt in self.students:
             print(studnt)
         
   
   
    def enroll(self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id=len(self.students)+1
            student=Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolld with id :{id},extra money {fee-6500}'
   
# ali=Student('asli',4,10)
# ran=Techer('ros','cse',205)
# print(ali)
# print(ran)
        
Phitron=School('Phitron')
Phitron.enroll('alia',5200)
Phitron.enroll('tlia',5300)
Phitron.enroll('blia',5500)
Phitron.add_techer('tom cruis','algo')
Phitron.add_techer('Bom cruis','DS')