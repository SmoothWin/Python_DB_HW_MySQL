class Book:
    author = ""
    publisher = ""
    publish_date = ""
    student_id = ""

    def __init__(self, author, publisher, publish_date, student_id):
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date
        self.student_id = student_id

    def to_dict(self):
        return {
            "author": self.author,
            "publisher": self.publisher,
            "publish_date": self.publish_date,
            "student_id": self.student_id
        }

