from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi .exceptions import HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from core.auth import create_token, decode_token
from core.config_bd import get_db
from models.login import Login
from models.usuario import Usuario
from core.config import SECRET_KEY, ALGORITHM

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users = {
    1048322496 : { "Usu_Id" : 1048322496, "Usu_Password" : "123456" }
}

@router.post('/login')
def login(form: Login):
    user = users.get(form.Usu_Id)

    if not user or user["Usu_Password"] != form.Usu_Password:
        raise HTTPException(status_code=404, detail="Usuario o contraseña incorrectos")

    token = create_token({ "Usu_Id": user["Usu_Id"] })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
