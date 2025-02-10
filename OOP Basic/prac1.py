class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avgMarks(self):
        n = len(self.marks)
        s = sum(self.marks)
        print(f"hi, {self.name}\nyour average marks is {s/n}")

s1 = Student("Magi Cuda", [97, 98, 99])
s1.avgMarks()