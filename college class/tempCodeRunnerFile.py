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
