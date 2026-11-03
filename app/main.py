from fastapi import FastAPI
from pydantic import BaseModel, StrictInt, StrictStr

class Subject(BaseModel):
    name: StrictStr

class Student(BaseModel):
    name: StrictStr
    grade: StrictInt

app = FastAPI()

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