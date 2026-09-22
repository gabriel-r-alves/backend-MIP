from sqlalchemy import Table, select

from .database import engine, Base


class Printer(Base):
    __tablename__ = "printers"
    __table__ = Table(__tablename__, Base.metadata, autoload_with=engine)

    
    def __repr__(self) -> str:
        return f"Printer(num_serial='{self.num_serial}', model='{self.model}', status='{self.status}', ip='{self.ip}', counter='{self.counter}', function='{self.printer_function}', last_modify='{self.last_modify}')"
    
    
    @classmethod
    def get_all(cls, session):
        stmt = select(cls).where(cls.active.is_(True))
        return session.scalars(stmt).all()


    @classmethod
    def get_by_serial(cls, printer_serial, session):
        stmt = select(cls).where(
            cls.active.is_(True)
            ,cls.num_serial == printer_serial
        )
        return session.execute(stmt).scalar_one_or_none()
    

class Branch(Base):
    __tablename__ = "branches"
    __table__ = Table(__tablename__, Base.metadata, autoload_with=engine)
    
    
    def __repr__(self) -> str:
        return f"Branch(Id='{str(self.id)}', Name='{self.name}')"
        
    
    @classmethod
    def get_all(cls, session):
        stmt = select(cls)
        return session.scalars(stmt).all()


    @classmethod
    def get_by_id(cls, branch_id, session):
        stmt = select(cls).where(
            cls.id == branch_id
        )
        return session.execute(stmt).scalar_one_or_none()
    
    
