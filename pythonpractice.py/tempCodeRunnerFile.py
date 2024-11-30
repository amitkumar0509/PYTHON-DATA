def get_detail_student(self, student_id):
        if student_id in self.students:
            return str(self.students[student_id])