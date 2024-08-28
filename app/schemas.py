from pydantic import BaseModel, Field, field_validator, model_validator
from datetime import datetime, time, date
from tortoise.contrib.pydantic import pydantic_model_creator

from app.models import Order


class OrderCreate(BaseModel):
    apartment_number: str
    pet_name: str
    pet_breed: str
    walk_date: date
    walk_time: time
    duration: int = Field(..., le=30)

    @field_validator('walk_date', mode='before')
    def validate_date(cls, value):
        try:
            return datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD-MM-YYYY.")


class OrderOutput(BaseModel):
    id: int
    apartment_number: str
    pet_name: str
    pet_breed: str
    walk_date: str
    walk_time: str
    duration: int

    @model_validator(mode='before')
    def convert_datetime_fields(cls, order):
        print(order)
        order.walk_date = order.walk_date.strftime("%d-%m-%Y")
        order.walk_time = order.walk_time.strftime("%H:%M")
        return order


OrderIn_Pydantic = pydantic_model_creator(Order, name="OrderIn", exclude_readonly=True)
