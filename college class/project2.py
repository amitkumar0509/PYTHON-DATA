# Class to represent a Student
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.student_id}, Grades: {self.grades}"

# Class to represent a Teacher
class Teacher:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        self.assigned_class = []
        self.subject = []

    def assign_subject(self, course):
        self.subject.append(course)

    def __str__(self):
        subjects_str = ", ".join([subject.course_name for subject in self.subject])
        return f"Teacher Name: {self.name}, ID: {self.employee_id}, Subjects: {subjects_str}"

# Class to represent a Course (subject)
class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def __str__(self):
        return f"Course Name: {self.course_name}"

# Class to represent a Classroom
class Classroom:
    def __init__(self, classroom_number):
        self.classroom_number = classroom_number
        self.student = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.student.append(student)

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)
        teacher.assigned_class.append(self)

    def add_course(self, course):
        self.courses.append(course)

    def get_class_details(self):
        print(f"\nClass: {self.classroom_number}")
        print("Teachers and their Subjects:")
        for teacher in self.teachers:
            subject_str = ", ".join([subject.course_name for subject in teacher.subject])
            print(f"- {teacher.name}: {subject_str}")
        print("\nStudents:")
        for student in self.student:
            print(f"- {student.name} (ID: {student.student_id}), Grades: {student.grades}")
        print()

# Class to represent a College
class College:
    def __init__(self):
        self.classes = {f"class_{i}": Classroom(f"class_{i}") for i in range(1, 13)}

    def get_classroom(self, class_name):
        return self.classes.get(class_name, None)

    def get_all_class_details(self, class_name):
        classroom = self.get_classroom(class_name)
        if classroom:
            classroom.get_class_details()
        else:
            print(f"Class {class_name} not found")

# Example Usage
college = College()

# Create teachers
teacher1 = Teacher("Sonika Alawat", "001")
teacher2 = Teacher("Jyoti", "002")
teacher3 = Teacher("Renuka", "003")
teacher4 = Teacher("Kirti", "004")

# Create students
student1 = Student("Amit", "001")
student2 = Student("Ankit", "002")
student3 = Student("Chandermani", "003")
student4 = Student("Dev", "004")

# Assign teachers and students to class_1
class_1 = college.get_classroom("class_1")
class_1.assign_teacher(teacher1)
class_1.assign_teacher(teacher2)
class_1.assign_teacher(teacher3)
class_1.assign_teacher(teacher4)

class_1.add_student(student1)
class_1.add_student(student2)
class_1.add_student(student3)
class_1.add_student(student4)

# Create courses
DSA = Course("Data Structure and Algorithm")
web_dev = Course("Web Development and IT")
DM = Course("Discrete Mathematics")
DE = Course("Digital Electronics")

# Add courses to the class
class_1.add_course(DSA)
class_1.add_course(web_dev)
class_1.add_course(DM)
class_1.add_course(DE)

# Assign subjects to teachers
teacher1.assign_subject(DSA)
teacher2.assign_subject(web_dev)
teacher3.assign_subject(DM)
teacher4.assign_subject(DE)

# Assign grades to students
student1.add_grade("DSA", "A")
student1.add_grade("DM", "A")
student1.add_grade("DE", "A")
student1.add_grade("web_dev", "A")

student2.add_grade("DSA", "A")
student2.add_grade("DM", "A")
student2.add_grade("DE", "A")
student2.add_grade("web_dev", "A")

student3.add_grade("DSA", "A")
student3.add_grade("DM", "A")
student3.add_grade("DE", "A")
student3.add_grade("web_dev", "A")

student4.add_grade("DSA", "A")
student4.add_grade("DM", "A")
student4.add_grade("DE", "A")
student4.add_grade("web_dev", "A")

# Get class details for class_1
college.get_all_class_details("class_1")
