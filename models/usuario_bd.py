from sqlalchemy import Column, Integer, String
from core.config_bd import Base

class Usuario(Base):
    __tablename__ = "usuario"

    Usu_Id = Column(Integer, primary_key=True, index=True)
    Usu_Nombre = Column(String(150), nullable=False)
    Usu_Email = Column(String(150), nullable=False)
    Usu_Telefono = Column(Integer, nullable=False)
    Rol_Id = Column(Integer, nullable=False)
    TpDoc_Id = Column(String(10), nullable=False)
    Usu_Password = Column(String(150), nullable=False)
