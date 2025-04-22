from school import School
from person import Student, Teacher
from Subject import Subject
from classroom import ClassRoom


school=School("Abs","Dhaka")

# Additing Classroom

eight=ClassRoom("Eight") 
Nine=ClassRoom("nine") 
ten=ClassRoom("Ten")

school.add_classroom(eight) 
school.add_classroom(Nine) 
school.add_classroom(ten) 