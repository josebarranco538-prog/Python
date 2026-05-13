from student import Student
from student_manager import StudentManager

manager = StudentManager()

s1 = Student(1, "Michael Ripoll")
s2 = Student(2, "Ana Perez")

manager.save_student(s1)
manager.save_student(s2)
manager.get_info()