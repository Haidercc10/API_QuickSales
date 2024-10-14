from pydantic import BaseModel, constr, conint

class Usuario(BaseModel):
     Usu_Id: conint(gt=10000, le=9999999999)
     Usu_Nombre: constr(min_length=1, max_length=150)
     Usu_Email: constr(min_length=1, max_length=150)
     Usu_Telefono: conint(gt=1000000, le=9999999999)
     Rol_Id: conint(gt=0, le=9999999999)
     TpDoc_Id: constr(min_length=1, max_length=10)
     Usu_Password : constr(min_length=1, max_length=50)

class UsuarioResponse(BaseModel):
     Usu_Id: int
     Usu_Nombre: str
     Usu_Email: str
     Usu_Telefono: int
     Rol_Id: int
     TpDoc_Id: str
     Usu_Password: str