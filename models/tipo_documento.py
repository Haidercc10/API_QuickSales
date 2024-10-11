from pydantic import BaseModel, constr, conint

class Tipo_Documento(BaseModel):
    TpDoc_Id : conint(gt=0, le=9999999999)
    TpDoc_Nombre : constr(min_length=1, max_length=50)
    TpDoc_Descripcion : constr(min_length=1, max_length=50)
