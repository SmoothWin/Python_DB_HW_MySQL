from DAL.DBData import DBData
from Entities.Student import Student


class DBStudents:
    dta = DBData()

    def select_all_students(self):
        return self.dta.execute_select_query("student")

    def select_student(self, student_id):
        return self.dta.execute_select_query("student", params={"student_id": student_id})

    def insert_student(self, student: Student):
        return self.dta.execute_insert_query("student", params=student)
