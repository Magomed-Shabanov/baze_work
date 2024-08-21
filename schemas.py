from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Схема для пользователя
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    orders: List['Order'] = []

    class Config:
        from_attributes = True

# Схема для товара
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

# Схема для заказа
class OrderBase(BaseModel):
    status: Optional[str] = "pending"

class OrderCreate(OrderBase):
    user_id: int
    product_id: int

class Order(OrderBase):
    id: int
    user_id: int
    product_id: int
    order_date: datetime

    class Config:
        from_attributes = True
