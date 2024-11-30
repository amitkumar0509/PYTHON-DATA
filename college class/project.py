class Student:
    def __init__(self,name,student_id):
        self.name= name
        self.student_id = student_id
        self.grades ={}
    def add_grade(self,course,grades):
        self.grades[course] = grades
    def __str__(self):
        return f"(Student name : {self.name} ,Student ID : {self.student_id},Grades:{self.grades}) "
    
class Teacher:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
        self.assigned_class = []
        self.subject = []
    def assign_sub(self,courses):
        self.subject.append(courses)
    def __str__(self):
        subjects_str = ", ".join([subject.course_name for subject in self.subjects]) 
        return f"(Teacher name : {self.name},Teacher Id: {self.employee_id},Subject =  {subjects_str})"

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

    def __str__(self):
         return f"Course Name: {self.course_name}"
        
class Classroom:
    def __init__(self, classroom_number):
        self.classroom_number = classroom_number
        self.students = []  
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)
        teacher.assigned_class.append(self) 

    def add_course(self, course):
        self.courses.append(course)
    def search_student(self,name,student_id):
        for student in self.students:
            if student.name == name and student.student_id == student_id:
                return student
    def get_class_details(self):
        print(f"\nClass: {self.classroom_number}")
        print("Teachers and their Subjects:")
        for teacher in self.teachers:
            subjects_str = ", ".join([subject.course_name for subject in teacher.subject])
            print(f"- {teacher.name}: {subjects_str}")
        print("\nStudents:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id}), Grades: {student.grades}")
        print()
class College:
    def __init__(self):
        self.classes = {"BTECH": Classroom("BTECH"),
                        "MTECH": Classroom("MTECH"),
                        "BCA": Classroom("BCA"),
                        "MCA": Classroom("MCA"),
                        "BSC" : Classroom("BSC")
                        

                        }  
    def get_classroom(self, class_name):
        return self.classes.get(class_name, None)
    def assign_teachers(self, teacher_list):
        # Automatically assign teachers to classrooms and subjects using a list
        for teacher_info in teacher_list:
            teacher_name, employee_id, class_name, subject_name = teacher_info
            teacher = Teacher(teacher_name, employee_id)
            classroom = self.get_classroom(class_name)
            if classroom:
                classroom.assign_teacher(teacher)  # Assign teacher to the class
                course = Course(subject_name)  # Create the course for the teacher
                classroom.add_course(course)  # Add the course to the classroom
                teacher.assign_sub(course)  # Assign the course to the teacher
            else:
                print(f"Class {class_name} not found")

    def get_all_class_details(self, class_name):
        classroom = self.get_classroom(class_name)
        if classroom:
            classroom.get_class_details()
            
        else:
            print(f"Class {class_name} not found")

teacher_list = [
    ("Sonika Alawat", "001", "BTECH", "Data Structure and Algorithm"),
    ("Jyoti", "002", "BTECH", "Web Development and IT"),
    ("Renuka", "003", "BTECH", "Discrete Mathematics"),
    ("Kirti", "004", "BTECH", "Digital Electronics"),
    ("Vikram", "005", "MTECH", "Machine Learning"),
    ("Nandini", "006", "MTECH", "Artificial Intelligence"),
    ("Ayesha Singh", "007", "BTECH", "Software Engineering"),
    ("Raj Patel", "008", "MTECH", "Cloud Computing"),
    ("Neha Kapoor", "009", "MBA", "Business Strategy"),
    ("Arun Verma", "010", "BTECH", "Cybersecurity")
]
college = College()

# Assign all teachers (including the new ones) to their respective classes and subjects
college.assign_teachers(teacher_list)

# Create students
student1 = Student("Amit", "001")
student2 = Student("Ankit", "002")
student3 = Student("Chandermani", "003")
student4 = Student("Dev", "004")
student5 = Student("Pooja", "005")
student6 = Student("Ravi", "006")

# Assign teachers and students to BTECH class
btech_class = college.get_classroom("BTECH")
mtech_class = college.get_classroom("MTECH")

btech_class.add_student(student1)
btech_class.add_student(student2)
btech_class.add_student(student3)
btech_class.add_student(student4)
mtech_class.add_student(student5)
mtech_class.add_student(student6)

# Create curses
DSA = Course("Data Structure and Algorithm")
web_dev = Course("Web Development and IT")
DM = Course("Discrete Mathematics")
DE = Course("Digital Electronics")

# Add courses to the BTECH class
btech_class.add_course(DSA)
btech_class.add_course(web_dev)
btech_class.add_course(DM)
btech_class.add_course(DE)

# Assign subjects to teachers


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
student5.add_grade("Machine Learning", "A")
student5.add_grade("Artificial Intelligence", "B")

student6.add_grade("Machine Learning", "B")
student6.add_grade("Artificial Intelligence", "A")


# Add new students to the BTECH class
new_student = Student("New Student", "005")
mayank = Student("Mayank", "2001")

btech_class.add_student(new_student)
btech_class.add_student(mayank)

# Get class details for BTECH class
college.get_all_class_details("BTECH")
college.get_all_class_details("MTECH")


# Search for a specific student
name = "Amit"
student_id = "001"
print(btech_class.search_student(name, student_id))

# Get class details for class_1

# Create a new student
new_student = Student("New Student", "005")
mayank  = Student("mayank","2001")
yashu = Student("yashu","32672")

# Add the new student to class_1
btech_class.add_student(new_student)
btech_class.add_student(mayank)
btech_class.add_student(yashu)
# Create a new student

name = "Amit"
student_id ="001"
print(btech_class.search_student(name,student_id))
#hii



    
        
    
