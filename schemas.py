from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class ProductBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)

class ProductCreate(ProductBase):          # lo que el cliente envía (sin id)
    pass

class ProductRead(ProductBase):            # lo que la API devuelve
    id: int
    model_config = ConfigDict(from_attributes=True)