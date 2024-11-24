"""from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from sqlalchemy import DECIMAL

T = TypeVar("T")

class LoginSchema(BaseModel):
    Prod_Id : Optional[int]  #conint(ge=0, le=9999999999)
    Prod_Nombre : Optional[str]  #constr(min_length=1, max_length=100)
    Prod_Descripcion : Optional[str]  #constr(min_length=1, max_length=100)
    Prod_Medida : Optional[str]  #constr(min_length=1, max_length=50)
    Prod_Precio : Optional[DECIMAL] = Field(ge=0.00, decimal_places=2)  #Optional[Decimal] = Field(ge=0.00, decimal_places=2)
    Und_Id : Optional[str]

class Config:
        orm_mode = True

        schema_extra = {
            "example":
                {
                    "Prod_Id" : 123456,
                    "Prod_Nombre" : "PRODUCTO 1",
                    "Prod_Descripcion" : "PRODUCTO 1",
                    "Prod_Medida" : "UNIDADES",
                    "Prod_Precio" : 100.00,
                    "Und_Id" : "UND"
                }
        }

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]"""