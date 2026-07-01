from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

products = [
    {
        "id": 1,
        "code": "SP001",
        "name": "Laptop Dell",
        "price": 15000000,
        "stock": 10
    },
    {
        "id": 2,
        "code": "SP002",
        "name": "Mouse Logitech",
        "price": 350000,
        "stock": 50
    }
]

class ProductCreate(BaseModel):
    code: str
    name: str
    price: float
    stock: int

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):

    # P1: chỉ ra lỗi bằng tét case 
    # Test case 1
    # Gửi request:
    # {
    #     "code": "SP001",
    #     "name": "Laptop HP",
    #     "price": 18000000,
    #     "stock": 5
    # }
    # Kết quả: API vẫn tạo thành công
    # Kết quả đúng: Phải báo lỗi vì mã SP001 đã tồn tại
    
    # đoạn code gây lỗi:
    # new_product = {
    #     ...
    # }
    # products.append(new_product)
    # Lý do:
    # API tạo và thêm sản phẩm ngay vào danh sách mà
    # khoongg kiểm tra code đã tồn tại hay chưa.

    # P2: Sửa code
    for item in products:
        if item["code"] == product.code:
            raise HTTPException(
                status_code=400,
                detail="Product code already exists"
            )

    new_product = {
        "id": len(products) + 1,
        "code": product.code,
        "name": product.name,
        "price": product.price,
        "stock": product.stock
    }

    products.append(new_product)

    return {
        "message": "Create product successfully",
        "data": new_product
    }