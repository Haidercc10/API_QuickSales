from fastapi import APIRouter, HTTPException, Depends
from fastapi.openapi.utils import status_code_ranges
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
import mysql.connector
from core.connection import connection

router = APIRouter()

users = {
    "Haider" : { "user_id" : "1048322496", "password" : "123456" }
}

@router.post('/login')
async def login(form_data : Annotated[OAuth2PasswordRequestForm, Depends()]):
    usuario = users.get(form_data.username)
    if not usuario:
        raise  HTTPException(status_code=404, detail="Usuario no encontrado")

    token = "xxxzzzyyy"
    return { "access_token" : token, "token_type": "bearer" }
