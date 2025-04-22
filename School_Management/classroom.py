class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.student = []  # list of student {"name":studentobj}
        self.subject = []  # list of suject {"eghit :subjectobjct"}

    def add_student(self, student):
        roll_id = f"{self.name}-{len(self.student)+1}"
        student.id = roll_id
        self.student.append(student)

    def add_subject(self, subject):
        self.subject.append(subject)

    def take_samister_final(self):
        for subject in self.subject:
            subject.exam(self.subject)
        for student in self.student:
            student.calculate_final_grade(self.student)
    