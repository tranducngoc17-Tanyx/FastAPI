from fastapi import FastAPI, Query, HTTPException, status
from typing import Optional, List, Dict, Any

app = FastAPI(title="Hệ thống Quản lý và Lọc sản phẩm")

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def get_products(
    # Khai báo Query Parameter: không bắt buộc (default = None)
    keyword: Optional[str] = Query(None, description="Từ khóa tìm kiếm theo tên"),
    max_price: Optional[float] = Query(None, description="Mức giá tối đa cần lọc")
):
    """
    API tìm kiếm sản phẩm theo tên và lọc theo mức giá tối đa.
    """
    
    # Kiểm tra xem người dùng có truyền max_price không và giá trị có hợp lệ không
    if max_price is not None and max_price < 0:
        # Nếu giá trị âm, trả về lỗi HTTP 400 Bad Request ngay lập tức
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="max_price không được âm"
        )
        
    filtered_products = products

    # Tình huống 1: Nếu người dùng truyền 'keyword'
    if keyword is not None:
        filtered_products = [
            prod for prod in filtered_products 
            if keyword.lower() in prod["name"].lower()       
        ]
    # Lọc danh sách: chuyển cả tên sản phẩm và keyword về chữ thường để so sánh (không phân biệt hoa/thường)    
    
    # Tình huống 2: Nếu người dùng truyền 'max_price'
    if max_price is not None:
        
        filtered_products = [
            prod for prod in filtered_products 
            if prod["price"] <= max_price
        ]   # Lọc danh sách: chỉ giữ lại những sản phẩm có giá nhỏ hơn hoặc bằng max_price
    # Trả về mảng các sản phẩm đã qua bộ lọc (Nếu không truyền tham số nào, tự động trả về hết)
    return filtered_products