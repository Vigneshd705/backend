from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"  # Example, adjust to your database config

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()

# Initialization function (optional if you're not using a DB)
async def init_db():
    print("Initializing database...")
    async with engine.begin() as conn:
        print("Connected to the database!")
        # Optionally create tables here (if using SQLAlchemy models)
        # await conn.run_sync(Base.metadata.create_all)
    print("Database initialization complete!")
