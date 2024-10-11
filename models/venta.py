from datetime import datetime, date
from pydantic import BaseModel, constr, conint

class Venta(BaseModel):
     Vta_Id : conint(gt=0, le=9999999999)
     Vta_Factura : constr(min_length=0, max_length=50)
     Vta_Fecha : date
     Vta_Hora : datetime
     Cli_Id : conint(gt=10000, le=9999999999)
     Usu_Id : conint(gt=10000, le=9999999999)
     Vta_Observacion : constr(min_length=0, max_length=200)