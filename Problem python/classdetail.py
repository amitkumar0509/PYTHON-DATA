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
        self.assigned_classes = []
        self.subjects = []

    def assign_class(self, classroom):
        self.assigned_classes.append(classroom)

    def assign_subject(self, course):
        self.subjects.append(course)

    def __str__(self):
        subjects_str = ", ".join([subject.course_name for subject in self.subjects])
        return f"Teacher Name: {self.name}, ID: {self.employee_id}, Subjects: {subjects_str}"

# Class to represent a Course (subject like Mathematics, English)
class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def __str__(self):
        return self.course_name

# Class to represent a Classroom for each grade
class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)
        teacher.assign_class(self)

    def add_course(self, course):
        self.courses.append(course)

    def get_class_details(self):
        print(f"\nClass: {self.class_name}")
        print("Teachers and their Subjects:")
        for teacher in self.teachers:
            subjects = ", ".join([subject.course_name for subject in teacher.subjects])
            print(f"- {teacher.name}: {subjects}")
        print("Students:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id}), Grades: {student.grades}")
        print()

# Class to manage multiple classrooms (Class 1 to 12)
class School:
    def __init__(self):
        self.classes = {f"Class {i}": Classroom(f"Class {i}") for i in range(1, 13)}

    def get_classroom(self, class_name):
        return self.classes.get(class_name, None)

    def get_all_class_details(self, class_name):
        classroom = self.get_classroom(class_name)
        if classroom:
            classroom.get_class_details()
        else:
            print(f"No data found for {class_name}")

# Example Usage
school = School()

# Create teachers
teacher1 = Teacher("Mr. Smith", "T001")
teacher2 = Teacher("Ms. Johnson", "T002")

# Create students
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

# Assign teachers and students to Class 3
class_3 = school.get_classroom("Class 3")
class_3.assign_teacher(teacher1)
class_3.assign_teacher(teacher2)

class_3.add_student(student1)
class_3.add_student(student2)

# Create courses
math = Course("Mathematics")
science = Course("Science")
english = Course("English")

# Add courses to the classroom
class_3.add_course(math)
class_3.add_course(science)
class_3.add_course(english)

# Assign subjects to teachers
teacher1.assign_subject(math)
teacher1.assign_subject(science)
teacher2.assign_subject(english)

# Add grades for students
student1.add_grade("Mathematics", "A")
student1.add_grade("Science", "B")
student1.add_grade("English", "A-")

student2.add_grade("Mathematics", "B+")
student2.add_grade("Science", "A")
student2.add_grade("English", "B")

# Retrieve details for Class 3
school.get_all_class_details("Class 3")
