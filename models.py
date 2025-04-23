from pydantic import BaseModel, Field, validator
from typing import List
import re

class Item(BaseModel):
    shortDescription: str = Field(..., pattern=r"^[\w\s\-]+$")
    price: str = Field(..., pattern=r"^\d+\.\d{2}$")

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-&]+$")
    purchaseDate: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")
    purchaseTime: str = Field(..., pattern=r"^\d{2}:\d{2}$")
    total: str = Field(..., pattern=r"^\d+\.\d{2}$")
    items: List[Item]

    @validator('items')
    def check_items_not_empty(cls, v):
        if not v:
            raise ValueError('items list must contain at least one item')
        return v
