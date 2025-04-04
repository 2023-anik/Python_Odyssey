class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __str__(self): # __str__ is used to define a string representation of the object
        return f"Student with name: {self.name}, {self.current_class}, {self.id}"
    

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self): #__repr__ is used to define a string representation of the object
        return f"Teacher: {self.name}, subject: {self.subject}, id: {self.id}"
    


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
    
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return f"not enough fee"
        else:
            id = len(self.students) + 1
            student = Student(name,  "C", id)
            self.students.append(student)
            return (
                f"Student {name} enrolled successfully\n"
                f"Extra money: {fee - 6500}\n"
            )
    def __repr__(self):
        result = (
            f"Welcome to {self.name}\n"
            f"---------{"our teacher".capitalize()}---------\n"
        )
        for teacher in self.teachers:
            result += f"{teacher}\n"
        
        result += f"---------{"our student".capitalize()}---------\n"
        
        for student in self.students:
            result += f"{student}\n"
        
        result += f"All Done for now\n"
        result += f"---------{"thank you".capitalize()}---------\n"
        
        return result



amr_school = School("Amr School")
amr_school.add_teacher("Mr. Rahim", "Math")
amr_school.add_teacher("Mr. Karim", "English")
amr_school.add_teacher("Mr. Akash", "Bangla")
amr_school.add_teacher("Mr. Shakib", "Science")

amr_school.enroll("Magi Suda", 7000)
amr_school.enroll("Shakib Al Hasan", 6000)
amr_school.enroll("Beissha Suda", 7000)
amr_school.enroll("Khanki Suda", 6000)
amr_school.enroll("Madar Suda", 6500)

print(amr_school)


school2 = School("Cudar School")
school2.add_teacher("Mr. Rahim", "Math")
school2.add_teacher("Mr. Karim", "English")

school2.enroll("Magi Suda", 7000)
school2.enroll("Shakib Al Hasan", 6000)
school2.enroll("Beissha Suda", 7000)

print(school2)