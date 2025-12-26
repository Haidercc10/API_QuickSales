from sqlalchemy.orm import Session
from core.security import hash_password
from models.usuario_bd import Usuario
from schemas.usuario_schema import Usuario


def crear_usuario(db: Session, data: Usuario):
    usuario = Usuario(
        Usu_Id=data.Usu_Id,
        Usu_Nombre=data.Usu_Nombre,
        Usu_Email=data.Usu_Email,
        Usu_Telefono=data.Usu_Telefono,
        Rol_Id=data.Rol_Id,
        TpDoc_Id=data.TpDoc_Id,
        Usu_Password=hash_password(data.Usu_Password)
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario
