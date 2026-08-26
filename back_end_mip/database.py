from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from .settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


def get_session():
    with SessionLocal() as session:
        yield session


class Base(DeclarativeBase):
    pass

        
if __name__ == "__main__":
    from models import Printer
    from sqlalchemy import select
    
    with SessionLocal() as session:
        printers = session.scalars(select(Printer).where(Printer.active.is_(False))).all()
        for printer in printers:
            print(printer)