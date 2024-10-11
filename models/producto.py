from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, constr, conint, Field


class Producto(BaseModel):
     Prod_Id : conint(gt=0, le=9999999999)
     Prod_Nombre : constr(min_length=1, max_length=100)
     Prod_Descripcion : constr(min_length=1, max_length=100)
     Prod_Medida : constr(min_length=1, max_length=50)
     Prod_Precio : Optional[Decimal] = Field(ge=0.00, decimal_places=2)
     Und_Id : constr(min_length=1, max_length=10)
