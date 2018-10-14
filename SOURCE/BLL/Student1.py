import sqlite3

conn = sqlite3.connect('CiscoLab.db')
with conn:
    c = conn.cursor()

class Student:
    def __init__(self, Name, StudNum, Course, Room, Professor):
        self.Name = Name
        self.StudNum = StudNum
        self.Course = Course
        self.Room = Room
        self.Professor = Professor
    
    def addStudInfo(self):
        c.execute("INSERT INTO StudentInfo VALUES (:Name, :StudentNumber, :Course, :Room, :Professor)",
                 {'Name': self.Name, 'StudentNumber': self.StudNum, 'Course': self.Course, 'Room': self.Room, 'Professor': self.Professor})
        conn.commit()

    def removeStudInfo(StudNum):
        c.execute("DELETE FROM StudentInfo WHERE StudentNumber=:sn", {'sn':StudNum})
        conn.commit()
        
    #def showBorrowed(self):
        