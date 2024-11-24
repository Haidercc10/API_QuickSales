from pydantic import conint, constr, BaseModel
from sqlalchemy import Column, Integer, String
from core.config_bd import Base

class Login(BaseModel):
    Usu_Id: conint(ge=10000, le=9999999999)
    Usu_Password : constr(min_length=1, max_length=50)

