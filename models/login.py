from sqlalchemy import Column, Integer, String
from core.config_bd import Base

class Login(Base):
    __tablename__ = "usuarios"

    Usua_Id = Column(Integer, primary_key = True, index=False)
    Usua_Password = Column(String(50))
    Rol_Id = Column(Integer)
