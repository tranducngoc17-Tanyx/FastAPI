from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()

products = [
    {"id": 1, "code": "SP001", "name": "Keyboard", "price": 500000, "stock": 10},
    {"id": 2, "code": "SP002", "name": "Mouse", "price": 300000, "stock": 5}
]

class ProductUpdate(BaseModel):
    code: str
    name: str
    price: float
    stock: int

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdate):

    # P1: phân tích & đề xuất giải pháp
    # Input:
    # product_id
    # code, name, price, stock
    
    # Output thành công: Thông tin sản phẩm sau khi cập nhật
    # Output thất bại:
    # -Product not found
    # -Product code already exists
    # -Name is required
    # -Price must be greater than 0
    # -Stock must be greater than or equal to 0
    
    # Giải pháp 1: Duyệt list để tìm sản phẩm rồi cập nhật
    # Giải pháp 2: Dùng dict với id làm key để tìm nhanh hơn

    # P2: So sánh & lựa chọn giải pháp
    # Duyệt list:
    # -Tìm kiếm: chậm hơn
    # -Bộ nhớ: ít
    # -Dễ hiểu: có
    # -Dễ bảo trì: có
    
    # Dùng dict:
    # -Tìm kiếm: nhanh
    # -Bộ nhớ: nhiều hơn
    # -Dễ hiểu: trung bình
    # -Dễ bảo trì: tốt
    
    # Kết luận: Chọn duyệt list vì dữ liệu nhỏ và dễ làm

    # P3; triển khai code
    product_found = None
    for item in products:
        if item["id"] == product_id:
            product_found = item
            break

    if product_found is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    for item in products:
        if item["code"] == product.code and item["id"] != product_id:
            raise HTTPException(
                status_code=400,
                detail="Product code already exists"
            )

    if product.name.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Name is required"
        )

    if product.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0"
        )

    if product.stock < 0:
        raise HTTPException(
            status_code=400,
            detail="Stock must be greater than or equal to 0"
        )

    product_found["code"] = product.code
    product_found["name"] = product.name
    product_found["price"] = product.price
    product_found["stock"] = product.stock

    return {
        "message": "Update product successfully",
        "data": product_found
    }