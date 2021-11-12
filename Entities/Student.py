class Student:
    def __init__(self, name, class_, subject):
        self.name = name
        self.class_ = class_
        self.subject = subject

    def to_dict(self):
        return {
            'student_name': self.name,
            'class': self.class_,
            'subject': self.subject
        }
