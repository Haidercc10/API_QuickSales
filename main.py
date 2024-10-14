from optparse import Values
from click import Tuple
from fastapi import FastAPI, HTTPException
import mysql.connector
from starlette.middleware.cors import CORSMiddleware
from core.connection import connection
from models.usuario import Usuario, UsuarioResponse

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return  { "message" : "Hello World" }

## Get users
@app.get('/usuarios')
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
@app.get('/usuario/{id}')
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
@app.post('/usuario')
async def post_usuario(usu : Usuario) :
    cursor = connection.cursor()
    query = "INSERT INTO Usuarios(Usu_Id, Usu_Nombre, Usu_Email, Usu_Telefono, Rol_Id, TpDoc_Id) VALUES(%s, %s, %s, %s, %s, %s)"
    values = (usu.Usu_Id, usu.Usu_Nombre, usu.Usu_Email, usu.Usu_Telefono, usu.Rol_Id, usu.TpDoc_Id)

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
@app.put('/usuario/{id}')
async def put_usuario(id:int, usu : Usuario) :
    cursor = connection.cursor()
    query = ("UPDATE Usuarios " 
             "SET Usu_Nombre = %s, " 
             "Usu_Email = %s, "
             "Usu_Telefono = %s, "
             "Rol_Id = %s, "
             "TpDoc_Id = %s "
             "WHERE Usu_Id = %s")
    values = (usu.Usu_Nombre, usu.Usu_Email, usu.Usu_Telefono, usu.Rol_Id, usu.TpDoc_Id, id)

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

## Delete user
@app.delete('/usuario/{id}')
async def delete_usuario(id) :
    cursor = connection.cursor()
    query = "DELETE FROM Usuarios WHERE Usu_Id = %s"
    values = id

    try:
        cursor.execute(query, (values))
        connection.commit()
        return { "message" : f"Usuario eliminado exitosamente!" }
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar usuario {err}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de tipado al eliminar usuario {e}")
    finally:
        cursor.close()



