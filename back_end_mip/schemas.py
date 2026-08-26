from typing import Optional
from pydantic import BaseModel


class Message(BaseModel):
    message: str


class PrinterPublic(BaseModel):
    num_serial: str
    model: Optional[str]
    branch_current_id: int
    ip: Optional[str]
    status: str
    counter: int
    

class ListPrinterPublic(BaseModel):
    printers: list[PrinterPublic]