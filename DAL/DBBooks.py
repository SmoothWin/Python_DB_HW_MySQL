from DAL.DBData import DBData
from Entities.Book import Book


class DBBooks:

    dta = DBData()

    def select_all_books(self):
        return self.dta.execute_select_query("book")

    def select_book(self, book_id):
        return self.dta.execute_select_query("book", params={"book_id": book_id})

    def insert_book(self, book: Book):
        return self.dta.execute_insert_query("book", params=book)

