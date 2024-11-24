from symtable import Class
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")

class LoginSchema(BaseModel):
    Usua_Id: Optional[int] = None
    Usua_Password: Optional[str] = None

    class Config:
        orm_mode = True

        schema_extra = {
            "example":
                {
                    "Usu_Id": 123456789,
                    "Usu_Password": "123456",
                }
        }

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T]