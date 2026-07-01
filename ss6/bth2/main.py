from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class createStudent(BaseModel):
    code: str | None
    name: str
    email: str
    age: int = Field(..., gt=0)


class updateStudent(BaseModel):
    code: str | None = None
    name: str | None = None
    email: str | None = None
    age: int | None = Field(None, gt=0)


app = FastAPI()
students = [
    {"id": 1, "code": "SV001", "name": "Nguyen Van A", "email": "a@gmail.com", "age": 20},
    {"id": 2, "code": "SV002", "name": "Tran Thi B", "email": "b@gmail.com", "age": 22},
    {"id": 3, "code": "SV003", "name": "Le Van C", "email": "c@gmail.com", "age": 18}
]


@app.get("/")
def root():
    return {"mess": "Hello"}


@app.get("/students")
def get_students(keyword: str | None = None,
                min_age: int | None = None,
                max_age: int | None = None):

    result = students
    if keyword is not None:
        result = [
            student for student in result
            if keyword.lower() in student["name"].lower()
            or keyword.lower() in student["code"].lower()
            or keyword.lower() in student["email"].lower()
        ]

    if min_age is not None:
        result = [
            student for student in result
            if student["age"] >= min_age
        ]

    if max_age is not None:
        result = [
            student for student in result
            if student["age"] <= max_age
        ]
    return result


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students")
def create_student(student: createStudent):

    for s in students:
        if s["code"] == student.code:
            raise HTTPException(status_code=400, detail="Code already exists")

    new_id = max((s["id"] for s in students), default=0) + 1

    new_student = {
        "id": new_id,
        "code": student.code,
        "name": student.name,
        "email": student.email,
        "age": student.age
    }

    students.append(new_student)
    return new_student

@app.put("/students/{student_id}")
def update_student(student_id: int, update_student: updateStudent):

    for student in students:

        if student["id"] == student_id:

            if update_student.code is not None:
                for s in students:
                    if s["code"] == update_student.code and s["id"] != student_id:
                        raise HTTPException(status_code=400, detail="Code already exists")
                student["code"] = update_student.code

            if update_student.name is not None:
                student["name"] = update_student.name

            if update_student.email is not None:
                student["email"] = update_student.email

            if update_student.age is not None:
                student["age"] = update_student.age

            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {"message": "Delete success"}

    raise HTTPException(status_code=404, detail="Student not found")