class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if self.width == self.height:
            self.type = 'Квадрат'
        else:
            self.type = 'Прямоугольник'

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def change_side(self, width, height):
        self.width = width
        self.height = height
        print('Выполнено!')
        if self.width == self.height:
            self.type = 'Квадрат'
        else:
            self.type = 'Прямоугольник'

    def info(self):
        print(f'''
Сторона а: {self.width}
Сторона b: {self.height}
Тип фигуры: {self.type}
Площадь: {self.area()}
Периметр: {self.perimeter()}
''')

r1 = Rectangle(10, 10)
r1.info()  

r2 = Rectangle(15, 5)
r2.info()  
print(r2.perimeter())
r2.change_side(5, 5)  
r2.info()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grades = []

#     def add_grade(self, grade):
#         self.grades.append(grade)

#     def average_grade(self):
#         if self.grades:
#             return sum(self.grades) / len(self.grades)
#         return 0

#     def __str__(self):
#         return f'Student: {self.name}, Age: {self.age}, Grades: {self.grades}'

# class StudentGroop:
#     def __init__(self):
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def remove_student(self, name):
#         self.students = [student for student in self.students if student.name != name]

#     def average_grade(self):
#         total_grades = 0
#         total_students = 0
#         for student in self.students:
#             if student.grades:
#                 total_grades += sum(student.grades)
#                 total_students += len(student.grades)
#         if total_students == 0:
#             return 0
#         return total_grades / total_students