class student():
    def __init__(self, surname, name, grade):
        self.surname = surname
        self.name = name
        self.grade = grade
        
students = []

with open('student_small.txt', 'r', encoding='utf-8)') as file:
    for line in file:
        data = line.split(' ')
        obj = students(data[0], data[1], int(data[2]))
        students.append(obj)  
        
for i in students:   