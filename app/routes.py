from fastapi import APIRouter, HTTPException, Path
from typing import List

from app.models import Order
from app.utils import parse_date
from app.validators import validate_order
from app.schemas import OrderOutput, OrderCreate
router = APIRouter()


@router.get("/orders/{date}", response_model=List[OrderOutput])
async def read_orders(date: str = Path(..., description="Date in DD-MM-YYYY format")):
    parsed_date = parse_date(date)
    orders = await Order.filter(walk_date=parsed_date).all()
    return orders


@router.post("/orders/")
async def create_order(order: OrderCreate):
    await validate_order(order)
    order_obj = await Order.create(**order.model_dump())
    return {"status": f"Заказ создан. ID: {order_obj.id}"}
