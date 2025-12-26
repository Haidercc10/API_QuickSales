from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi .exceptions import HTTPException
from core.auth import create_token, get_current_user
from models.login import Login

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users = {
    1048322496 : { "Usu_Id" : 1048322496, "Usu_Password" : "123456" }
}

@router.post('/login')
def login(form: Login):
    user = users.get(form.Usu_Id)

    if not user or user["Usu_Password"] != form.Usu_Password:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")

    token = create_token({ "sub": str(user["Usu_Id"]) })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/profile")
def profile(user_id: str = Depends(get_current_user)):
    return {
        "message": "Ruta protegida",
        "user_id": user_id
    }
