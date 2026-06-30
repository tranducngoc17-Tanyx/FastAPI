from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from typing import List

app = FastAPI(title="Hệ thống Đăng ký Học viên")

students_db = [
    {
        "full_name": "Tran Van B",
        "email": "existing@gmail.com",
        "age": 22,
        "course": "python",
        "phone": "0123456789"
    }
]

class StudentCreate(BaseModel):
    full_name: str = Field(..., min_length=3, description="Họ tên không được trống và ít nhất 3 ký tự")
    email: EmailStr = Field(..., description="Email học viên phải đúng định dạng")
    
    age: int = Field(..., ge=0, description="Tuổi học viên không được là số âm")
    course: str = Field(..., description="Khóa học đăng ký")
    phone: str = Field(..., description="Số điện thoại liên hệ")


@app.post("/students", status_code=status.HTTP_201_CREATED)
def register_student(student_data: StudentCreate):
    """
    API tiếp nhận request body, kiểm tra trùng lặp email và thêm mới học viên.
    """
    input_email = student_data.email
    
    for student in students_db:
        if student["email"] == input_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email đã tồn tại trong hệ thống"
            )
            
    new_student = student_data.model_dump()
    students_db.append(new_student)
    
    # Trả về kết quả thành công và thông tin học viên mới tạo
    return {
        "message": "Đăng ký học viên thành công",
        "student": new_student
    }   