from pydantic import BaseModel, constr

class Unidades_Medidas(BaseModel):
    Und_Id: constr(min_length=1, max_length=10)
    Und_Nombre: constr(min_length=1, max_length=50)
    Und_Descripcion: constr(min_length=1, max_length=50)