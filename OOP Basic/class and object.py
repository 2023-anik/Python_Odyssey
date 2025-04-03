class Student:
    # name = "Rahim"
    college_name = "Daffodil International University"

    #Default constructor
    def __init__(self):
        pass

    #Parameterized constructor
    def __init__(self, fullname, marks): #self is a reference to the current instance of the class
        self.fullname = fullname
        self.marks = marks
        print(self)
        print("adding new student in Database..")
    
    @staticmethod # decorator to make hello a static method
    def hello(): # hello is a static method of Student class
        print("Hello, world")

    def welcome(self): # hello is a method of Student class
        print("Welcome,", self.fullname)

# s1 = Student() # creating object of Student class
# s1 is a reference to the current instance of the class
s1 = Student("Magi Cuda", 97)
print(s1)
print(Student.college_name) # accessing class variable using class name
print(s1.fullname, s1.marks) # accessing class variable using object
s1.hello() # calling static method of Student class using object
s1.welcome() # calling method of Student class using object


#here, self.fullname and self.marks are instanace attributes means they are unique for each object
# college_name is a class attribute means it is common for all objects of the class