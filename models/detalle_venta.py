
from pydantic import BaseModel, constr, conint, Field
from typing import Optional
from decimal import Decimal

class Detalle_Venta(BaseModel):
     DtVta_Codigo : conint(gt=0, le=9999999999)
     Vta_Id : conint(gt=0, le=9999999999)
     Prod_Id : conint(gt=0, le=9999999999)
     DtVta_Cantidad : Optional[Decimal] = Field(ge=0.00, decimal_places=2)
     Und_Id : constr(min_length=1, max_length=50)
     DtVta_Precio : Optional[Decimal] = Field(ge=0.00, decimal_places=2)