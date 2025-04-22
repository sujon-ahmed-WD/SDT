class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {} # {"bangla" : teacher_object}
        self.classrooms = {} # {"eight" : classroom_object}
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] =  teacher
    def student_admission(self, student):
         classname=student.classroom.name
         self.classrooms[classname].add_student(student)
    
    # rahim - bang - 50 - B - 2.00
    #       - eng  - 80 - A+ - 5.00
    # ------------------------
    # total ----------- - C - 2.00
    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks >= 70 and marks<80:
            return 'A'
        elif marks >= 60 and marks <70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    @staticmethod
    def value_to_grade(value):
        if value >=4.5 and value <=5.00:
            return 'A+'
        elif value >=3.5 and value <=4.50:
            return 'A'
        elif value >=3.0 and value <=3.5:
            return  'A-'
        elif value >=2.5 and value <=3.0:
            return 'B'
        elif value >=2.0 and value <2.5:
            return 'C'
        elif value >=2.0 and value <2.5:
            return 'D'
        else:
            return 'F'
    
    def __repr__(self):
        # All Classroom
        for key in self.classrooms.keys():
            print(key)
        # All Student
        print("All Student")
        result=' '
        for key,value in self.classrooms.items():      # prottketa  calssroom e galtm
            
            result+=f"----------     {key.upper()}  classroom Students\n--------" #  Student name dakhba .... 
            for student in value.student:
                result+=f"{student.name}\n"
                
        print(result)
        
        # All Sujbect
        print("ALL subject")
        subject =''
        for key,value in self.classrooms.items(): # protekka classrooma e galam
            
            subject+=f"{key.upper()} classroom subject\n"
            for  sub in value.subject:
                subject+=f"{sub.name}\n"           
        print(subject)    
        
        # All Teacher 
        for key in self.teachers.keys():
            print(key)
         
        # All Student
        print("student result")
        
        for key,value in self.classrooms.items():
            for student in value.student:
                 for k,i in student.marks.items():
                     print(student.name,k,i,student.subject_grade[k])
        
        
        
        
        
        
        
        
 
 
    