import sqlite3
from student import Student

conn = sqlite3.connect('StudentTable2.db')

c = conn.cursor()

c.execute("""CREATE TABLE users2 (
        First text,
        Last text,
        StudentNumber int,
        Course text, Section text, Room text, Professor text
        )""")

def insert_stud(stud):
    with conn:
        c.execute("INSERT INTO users2 VALUES (:First,:Last,:StudentNumber,:Course,:Section,:Room,:Professor)",
          {'First':stud.First, 'Last':stud.Last, 'StudentNumber':stud.Student, 'Course':stud.Course,
           'Section':stud.Section, 'Room':stud.Room, 'Professor':stud.Professor})
        
def get_stud_by_name(lastname):
    c.execute("SELECT * FROM users2 WHERE Last=:Last",{'Last':lastname})
    return c.fetchall()

def update_sn(stud,Student):
    with conn:
        c.execute("""UPDATE users2 SET StudentNumber =: StudentNumber WHERE First=:First AND 
                  Last=:Last""", {'First':stud.First, 'Last':stud.Last})

def remove_stud(stud):
    with conn:
        c.execute("DELETE from users2 WHERE First=:First AND Last=:Last", 
                  {'First':stud.First, 'Last':stud.Last})
        
stud_1 = Student('Erwin', 'Milan', 2014101852,'ECE161L', 'A1', 'N107','Dimaunahan')
stud_2 = Student('Rachel', 'Fernando', 2014105557, 'ECE160L', 'A1', 'N107', 'Aseron')
stud_3 = Student('Shannen', 'Villanueva', 2014102239, 'ECE161L', 'B2', 'N208', 'Pahutan')

insert_stud(stud_1)
insert_stud(stud_2)
insert_stud(stud_3)


conn.commit()
conn.close()

