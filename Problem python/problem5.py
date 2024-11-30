class student:
    def __init__(self,name,std_id):
        self.std_id = std_id
        self.name = name
        self.courses=[]
    def enroll_crse(self,course):
        self.courses.append(course)
        course.add_student(self)
    def __str__(self):
        return f"Student Name: {self.name}, ID: {self.std_id}"
class course:
    def __init__(self,course_id,course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students=[]
        self.teacher = None
    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
    def assgn_teacher(self,teacher):
        self.teacher = teacher
        teacher.assgn_teacher(self)
    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}"
class Teacher:
    def __init__(self, name,teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.course = []
    def assgn_teacher(self,course):
        if  course not in self.course:
            self.course.append(course)
    def grade_student(self, student, course, grade):
        if course in self.courses and student in course.students:
            print(f"{student.name} received a grade of {grade} in {course.course_name}.")
        else:
            print(f"{student.name} is not enrolled in {course.course_name} or you do not teach this course.")

    def __str__(self):
        return f"Teacher Name: {self.name}, ID: {self.employee_id}"
    
student1 = student("Amit","A001")
student2 = student("tanzil","A002")
student3 = student("yashu","A003")
course1 = course("c001","Mathematics")
teacher1 = Teacher("Renuka","233")
student1.enroll_crse(course1)
student2.enroll_crse(course1)
student3.enroll_crse(course1)
print(course1)
