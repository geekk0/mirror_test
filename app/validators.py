from fastapi import HTTPException

from app.models import Order
from app.schemas import OrderCreate


async def validate_order(order: OrderCreate):
    if order.walk_time.minute not in [0, 30]:
        raise HTTPException(status_code=400, detail="Прогулка может начинаться либо в начале часа, либо в половину")
    if order.walk_time.hour < 7 or order.walk_time.hour > 22:
        raise HTTPException(status_code=400, detail="Прогулки доступны с 7.00 до 23.00.")

    existing_orders = await Order.filter(walk_date=order.walk_date, walk_time=order.walk_time).all()
    print(existing_orders)
    if len(existing_orders) >= 2:
        raise HTTPException(status_code=400, detail="Уже назначено максимальное количество прогулок на это время.")
