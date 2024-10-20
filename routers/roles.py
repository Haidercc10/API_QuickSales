from fastapi import APIRouter, HTTPException
from optparse import Values
from click import Tuple
import mysql.connector
from core.connection import connection
from models.rol import Roles, RolesResponse

router = APIRouter()

## Get Roles
@router.get('/roles')
async def get_roles():
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM Roles"

    try:
        cursor.execute(query)
        roles = cursor.fetchall()
        return roles

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error de mysql : {err}")
    finally:
        cursor.close()