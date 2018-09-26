class Student:

    def __init__(self, First, Last, Student, Course, Section, Room, Professor):
        self.First = First
        self.Last = Last
        self.Student = Student
        self.Course = Course
        self.Section = Section
        self.Room = Room
        self.Professor = Professor

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.First, self.Last)

    @property
    def fullname(self):
        return '{} {}'.format(self.First, self.Last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.First, self.Last, self.Student)