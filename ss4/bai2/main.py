from enum import Enum
from fastapi import FastAPI, HTTPException, status
from typing import List, Dict, Any

app = FastAPI()

class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"

orders = [
    {"id": 1, "customer_name": "Nguyễn Văn An", "total": 250000, "status": "pending"},
    {"id": 2, "customer_name": "Trần Thị Bình", "total": 500000, "status": "paid"},
    {"id": 3, "customer_name": "Lê Văn Cường", "total": 150000, "status": "cancelled"},
    {"id": 4, "customer_name": "Phạm Thị Dung", "total": 320000, "status": "pending"}
]


@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    valid_statuses = [s.value for s in OrderStatus]
    if status not in valid_statuses:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Trạng thái đơn hàng không hợp lệ"
        )
    
    filtered_orders = [order for order in orders if order["status"] == status]
    return filtered_orders

