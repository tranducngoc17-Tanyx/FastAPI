from fastapi import FastAPI
app = FastAPI(title="Product API", description="API xử lý chi tiết sản phẩm bằng Path Parameter")

products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 350000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]

# thêm cặp dấu {} vào đường dẫn để biến nó thành Path Parameter
@app.get("/products/{product_id}")
def get_product_detail(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {
        "message": "Không tìm thấy sản phẩm"
    }