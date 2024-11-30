class Student:
    def __init__(self, student_id, name):
        self.name = name
        self.student_id = student_id
        self.grades = {}
        
    def add_grade(self, course, grade):
        self.grades[course] = grade
        
    def get_grades(self):
        return self.grades
    
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grades: {self.grades}"
    

class Classroom:
    def __init__(self):
        self.students = {}
        
    def enroll_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        else:
            print(f"Student {name} already exists")
            
    def record_grade(self, student_id, course, grade):
        if student_id in self.students:
            self.students[student_id].add_grade(course, grade)
            print(f"Grade {grade} recorded for student ID {student_id} in course {course}.")
        else:
            print(f"Student ID {student_id} does not exist")
            
    def get_detail_student(self, student_id):
        if student_id in self.students:
            return str(self.students[student_id])
        else:
            print(f"Student ID {student_id} does not exist")
            return None
            
    def get_all_students(self):
        return [str(student) for student in self.students.values()]


classroom = Classroom()
classroom.enroll_student(1, "Amit")
classroom.enroll_student(2, "Arya")

classroom.record_grade(2, "Math", 90)
classroom.record_grade(1, "Science", 85)
classroom.record_grade(1, "English", 95)

print(classroom.get_detail_student(2))
print(classroom.get_detail_student(1))

print("All students:")
for student_info in classroom.get_all_students():
    print(student_info)
