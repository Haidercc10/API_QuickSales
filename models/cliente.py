from pydantic import BaseModel, constr, conint

class Cliente(BaseModel):
     Cli_Id : conint(gt=10000, le=9999999999)
     Cli_Name : constr(min_length=1, max_length=150)
     Cli_Telefono : conint(gt=1000000, le=9999999999)
     Cli_Email :  constr(min_length=1, max_length=150)
     Cli_Direccion : constr(min_length=1, max_length=150)
     Cli_Ciudad : constr(min_length=1, max_length=50)
     TpDoc_Id : constr(min_length=1, max_length=10)