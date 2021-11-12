from DAL.DBBooks import DBBooks
from DAL.DBStudents import DBStudents
from DAL.DBData import DBData
from Entities.Book import Book
from Entities.Student import Student

books = DBBooks()
students = DBStudents()

id_number = 1
# BOOKS
books_getAll = books.select_all_books()
book_getById = books.select_book(id_number)
book_insert = Book("Johnny Saint", "BRZ", "2420", None)
books.insert_book(book_insert)

print("Book Inserted : " + str(book_insert.author))
print("List of all books : " + str(books_getAll))
print("Book with the id: " + str(id_number) + str(book_getById))


#STUDENTS
students_getAll = students.select_all_students()
student_getById = students.select_student(id_number)
student_insert = Student("Johnny Sins", "Bad Class", "A-699")
students.insert_student(student_insert)

print("Student Inserted : " + str(student_insert.name))
print("List of all students : " + str(students_getAll))
print("Student with the id: " + str(id_number) + str(student_getById))
