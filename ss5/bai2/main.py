from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

enrollments = [
    {
        "id": 1,
        "student_id": "SV001",
        "course_id": 1
    },
    {
        "id": 2,
        "student_id": "SV002",
        "course_id": 1
    }
]

class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: int

@app.post("/enrollments", status_code=status.HTTP_201_CREATED)
def create_enrollment(enrollment: EnrollmentCreate):

    # Phần 1: chỉ ra lỗi
    # Test 1:
    # student_id = "SV001", course_id = 1 -> Vẫn đăng ký được
    # Đúng phải báo lỗi vì đã đăng ký khóa học

    # Test 2:
    # Gửi lại:
    # student_id = "SV002", course_id = 1 -> Vẫn tạo bản ghi mới
    # Đúng phải báo lỗi

    # Lỗi ở đoạn dưới vì thêm dữ liệu luôn,
    # không kiểm tra student_id và course_id đã tồn tại.

    # Phần 2: Sửa
    for item in enrollments:
        if item["student_id"] == enrollment.student_id and item["course_id"] == enrollment.course_id:
            raise HTTPException(
                status_code=400,
                detail="Student already enrolled in this course"
            )

    new_enrollment = {
        "id": len(enrollments) + 1,
        "student_id": enrollment.student_id,
        "course_id": enrollment.course_id
    }
    enrollments.append(new_enrollment)

    return {
        "message": "Enroll successfully",
        "data": new_enrollment
    }