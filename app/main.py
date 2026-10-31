from fastapi import FastAPI
from pydantic import BaseModel, StrictStr

class Subject(BaseModel):
    name: StrictStr
app = FastAPI()

subjects = ["Physics", "Chemistry", "Mathematics"]

@app.get("/subjects")
def get_subjects():
    return  {
        "subjects" : subjects
        }

@app.post("/add_subject")
def add_subject(subject: Subject):
    subjects.append(subject.name)
    return {
        "subjects": subjects
    }