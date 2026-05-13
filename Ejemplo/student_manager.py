

class StudentManager:
    def __init__(self):
        self.student_list = []

    def save_student(self, student):
        self.student_list.append(student)

    def get_info(self):
        for i in self.student_list:
            print(f"Id: {i.id} \nName: {i.name}\n")


