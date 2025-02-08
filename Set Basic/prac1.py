#You are given a list of subjects for students. Assume one classroom is required for 1 subject. HOw many classrooms are needed by all students.

subjects = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"]
classrooms = set()
for sub in subjects:
    classrooms.add(sub)

print(len(classrooms))