from pydantic import BaseModel, constr, conint

class Roles(BaseModel):
    Rol_Id: conint(gt=0, le=9999999999)
    Rol_Nombre: constr(min_length=1, max_length=50)
    Rol_Descripcion: constr(min_length=1, max_length=50)

class RolesResponse(BaseModel):
    Rol_Id: conint(gt=0, le=9999999999)
    Rol_Nombre: constr(min_length=1, max_length=50)
    Rol_Descripcion: constr(min_length=1, max_length=50)