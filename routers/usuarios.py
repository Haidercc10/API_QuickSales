from fastapi import APIRouter, HTTPException
from optparse import Values
from click import Tuple
import mysql.connector
from core.connection import connection
from models.usuario import Usuario, UsuarioResponse

router = APIRouter()

## Get users
@router.get('/usuarios')
async def get_usuarios():
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM Usuarios"

    try:
        cursor.execute(query)
        usuarios = cursor.fetchall()
        return usuarios

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error de mysql : {err}")
    finally:
        cursor.close()

## Get user
@router.get('/usuarios/{id}')
async def get_usuario(id):
    cursor = connection.cursor()

    query = "SELECT Usu_Id, Usu_Nombre, Usu_Email, Usu_Telefono, Rol_Id, TpDoc_Id, Usu_Password FROM Usuarios WHERE Usu_Id = %s"
    values = id

    try:
        cursor.execute(query, [values])
        usuario = cursor.fetchone()

        return UsuarioResponse(
            Usu_Id=usuario[0],
            Usu_Nombre=usuario[1],
            Usu_Email=usuario[2],
            Usu_Telefono=usuario[3],
            Rol_Id=usuario[4],
            TpDoc_Id=usuario[5],
            Usu_Password=usuario[6],
        )

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error de mysql 1: {err}")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Usuario no encontrado: {e}")
    finally:
        cursor.close()

## Create user
@router.post('/usuarios')
async def post_usuario(usu : Usuario) :
    cursor = connection.cursor()
    query = "INSERT INTO Usuarios(Usu_Id, Usu_Nombre, Usu_Email, Usu_Telefono, Rol_Id, TpDoc_Id, Usu_Password) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (usu.Usu_Id, usu.Usu_Nombre, usu.Usu_Email, usu.Usu_Telefono, usu.Rol_Id, usu.TpDoc_Id, usu.Usu_Password)

    try:
        cursor.execute(query, values)
        connection.commit()
        return { "message" : f"Usuario {usu.Usu_Nombre} creado exitosamente!" }
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar usuario {err}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de tipado al registrar usuario {e}")
    finally:
        cursor.close()

## Update user
@router.put('/usuarios/{id}')
async def put_usuario(id:int, usu : Usuario) :
    cursor = connection.cursor()
    query = ("UPDATE Usuarios " 
             "SET Usu_Nombre = %s, " 
             "Usu_Email = %s, "
             "Usu_Telefono = %s, "
             "Rol_Id = %s, "
             "TpDoc_Id = %s, "
             "Usu_Password = %s "
             "WHERE Usu_Id = %s")
    values = (usu.Usu_Nombre, usu.Usu_Email, usu.Usu_Telefono, usu.Rol_Id, usu.TpDoc_Id, usu.Usu_Password, id)

    try:
        cursor.execute(query, tuple(values))
        connection.commit()
        return { "message" : f"Usuario actualizado exitosamente!" }
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar usuario {err}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de tipado al actualizar usuario {e}")
    finally:
        cursor.close()



