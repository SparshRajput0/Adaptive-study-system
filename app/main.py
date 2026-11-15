import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel, StrictInt, StrictStr

class Subject(BaseModel):
    name: StrictStr

class Student(BaseModel):
    name: StrictStr
    grade: StrictInt

# data base connection
connection = sqlite3.connect("study_app.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, class INTEGER, exam_goal TEXT)")
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
cursor.execute(
    "INSERT INTO students (name, class, exam_goal)"
    "VALUES ('sparsh', 11, 'MEXT & JEE');"
    )
cursor.execute("SELECT * FROM students")
connection.commit()
app = FastAPI()

# test only
print(cursor.fetchall())

subjects_data = ["Physics", "Chemistry", "Mathematics"]

students_data = []

#SUBJECTS METHODS
@app.get("/subjects")
def get_subjects():
    return  {
        "subjects" : subjects_data
        }

@app.post("/subjects")
def add_subject(subject: Subject):
    subjects_data.append(subject.name)
    return {
        "subjects": subjects_data
    }

#STUDENT METHODS
@app.get("/students")
def get_students():
    return{
        "students": students_data
    }

@app.post("/students")
def add_student(student: Student):
    new_student = {
        "name": student.name,
        "grade": student.grade
    }
    students_data.append(new_student)
    return{
        "students": students_data
    }