from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Создаем асинхронный двигатель для SQLite базы данных
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Создаем базовый класс для моделей
Base = declarative_base()

async def init_db():
    # Импорт моделей перед созданием таблиц
    from models import User, Product, Order
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
