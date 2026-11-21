import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel, StrictInt, StrictStr

class Subject(BaseModel):
    name: StrictStr

class Student(BaseModel):
    name: StrictStr
    class_: StrictInt
    exam_goal: StrictStr

# DATABASE
connection = sqlite3.connect(
    "study_app.db",
    check_same_thread= False
)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, class INTEGER, exam_goal TEXT)")
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
connection.commit()

app = FastAPI()

# #SUBJECTS METHODS
# @app.get("/subjects")
# def get_subjects():
#     return  {
#         "subjects" : subjects_data
#         }

# @app.post("/subjects")
# def add_subject(subject: Subject):
#     subjects_data.append(subject.name)
#     return {
#         "subjects": subjects_data
#     }

#STUDENT METHODS
@app.get("/students")
def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return{
        "students": students
    }

@app.post("/students")
def add_student(student: Student):
    cursor.execute("INSERT INTO students (name, class, exam_goal) VALUES (?, ?, ?)", (student.name, student.class_, student.exam_goal))
    connection.commit()
    return{
        "status":"updated succesfuly✅"
    }