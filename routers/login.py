from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from fastapi .exceptions import HTTPException
from jose import jwt
from sqlalchemy.orm import Session
from core.config_bd import get_db
from models.login import Login
from models.usuario import Usuario

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users = {
    1048322496 : { "Usu_Id" : 1048322496, "Usu_Password" : "123456" }
}

def encode_token(payload: dict) -> str:
    token = jwt.encode(payload, key="secret", algorithm="HS256")
    return token

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    data = jwt.decode(token, key="secret", algorithms=["HS256"])
    return data


@router.post('/login_json')
def login(form_data: Login):
    user = users.get(form_data.Usu_Id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    token = encode_token({ "Usu_Id": user["Usu_Id"] })
    return { "access_token": token, "token_type": "bearer" }

""""@router.post('/login')
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    token = encode_token({ "username": user["username"] })
    return { "access_token": token, "token_type": "bearer" }"""

@router.get('/login/profile')
def profile(my_user: Annotated[dict, Depends(decode_token)]):
    return  my_user

