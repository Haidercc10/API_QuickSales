from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, constr, conint, Field


class Stock_Producto(BaseModel):
     Sto_Id : conint(gt=0, le=9999999999)
     Prod_Id : conint(gt=0, le=9999999999)
     Sto_Cantidad : Optional[Decimal] = Field(ge=0.00, decimal_places=2)
     Und_Id : constr(min_length=1, max_length=10)
     Sto_Ubicacion : constr(min_length=1, max_length=50)