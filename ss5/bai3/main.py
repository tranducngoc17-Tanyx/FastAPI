from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()

students = [
    {"id": 1, "name": "Nguyen Van A"},
    {"id": 2, "name": "Tran Thi B"},
    {"id": 3, "name": "Le Van C"}
]

courses = [
    {"id": 1, "name": "FastAPI Basic", "capacity": 2},
    {"id": 2, "name": "Python OOP", "capacity": 2}
]

registrations = [
    {"id": 1, "student_id": 1, "course_id": 1},
    {"id": 2, "student_id": 2, "course_id": 1}
]

class RegistrationCreate(BaseModel):
    student_id: int
    course_id: int

@app.post("/registrations", status_code=status.HTTP_201_CREATED)
def create_registration(registration: RegistrationCreate):

    # P1: Phân tích và thiết kế
    # Input:
    # student_id
    # course_id
    
    # Output thành công:
    # HTTP 201
    # Thông tin đăng ký mới
    
    # Output thất bại:
    # Student not found
    # Course not found
    # Student already registered this course
    # Course is full
    
    # Giải pháp:
    # 1 Kiểm tra học viên tồn tại
    # 2 Kiểm tra khóa học tồn tại
    # 3 Kiểm tra đăng ký trùng
    # 4 Kiểm tra khóa học còn chỗ
    # 5 Thêm đăng ký mới

    # P2: Triển khai code
    # Kiểm tra học vin 
    student_exists = False
    for student in students:
        if student["id"] == registration.student_id:
            student_exists = True
            break

    if not student_exists:
        raise HTTPException(
            status_code=400,
            detail="Student not found"
        )

    # Kiểm tra khóa học
    course = None
    for item in courses:
        if item["id"] == registration.course_id:
            course = item
            break

    if course is None:
        raise HTTPException(
            status_code=400,
            detail="Course not found"
        )

    # Kiểm tra đăng ký trùng
    for item in registrations:
        if item["student_id"] == registration.student_id and item["course_id"] == registration.course_id:
            raise HTTPException(
                status_code=400,
                detail="Student already registered this course"
            )

    # Kiểm tra sĩ số
    count = 0
    for item in registrations:
        if item["course_id"] == registration.course_id:
            count += 1

    if count >= course["capacity"]:
        raise HTTPException(
            status_code=400,
            detail="Course is full"
        )

    new_registration = {
        "id": len(registrations) + 1,
        "student_id": registration.student_id,
        "course_id": registration.course_id
    }

    registrations.append(new_registration)

    return {
        "message": "Register successfully",
        "data": new_registration
    }