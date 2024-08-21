from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Product, Order
from schemas import UserCreate, ProductCreate, OrderCreate

# CRUD операции для пользователей
async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

# CRUD операции для товаров
async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).filter(Product.id == product_id))
    return result.scalars().first()

async def get_products(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    return result.scalars().all()

# CRUD операции для заказов
async def create_order(db: AsyncSession, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

async def get_order(db: AsyncSession, order_id: int):
    result = await db.execute(select(Order).filter(Order.id == order_id))
    return result.scalars().first()

async def get_orders(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Order).offset(skip).limit(limit))
    return result.scalars().all()
