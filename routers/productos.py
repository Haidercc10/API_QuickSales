from fastapi import APIRouter, HTTPException
from optparse import Values
from click import Tuple
import mysql.connector
from core.connection import connection
from models.producto import Producto, ProductoResponse

router = APIRouter()

## Get products
@router.get('/productos')
async def get_productos():
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM Productos"

    try:
        cursor.execute(query)
        productos = cursor.fetchall()
        return productos

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error de mysql : {err}")
    finally:
        cursor.close()

## Get product
@router.get('/productos/{id}')
async def get_productos(id):
    cursor = connection.cursor()

    query = "SELECT Prod_Id, Prod_Nombre, Prod_Descripcion, Prod_Medida, Prod_Precio, Und_Id FROM Productos WHERE Prod_Id = %s"
    values = id

    try:
        cursor.execute(query, [values])
        producto = cursor.fetchone()

        return ProductoResponse(
            Prod_Id=producto[0],
            Prod_Nombre=producto[1],
            Prod_Descripcion=producto[2],
            Prod_Medida=producto[3],
            Prod_Precio=producto[4],
            Und_Id=producto[5],
        )

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error de mysql 1: {err}")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Producto no encontrado: {e}")
    finally:
        cursor.close()

## Create product
@router.post('/productos')
async def post_productos(prod : Producto) :
    cursor = connection.cursor()
    query = "INSERT INTO Productos(Prod_Id, Prod_Nombre, Prod_Descripcion, Prod_Medida, Prod_Precio, Und_Id) VALUES(%s, %s, %s, %s, %s, %s)"
    values = (prod.Prod_Id, prod.Prod_Nombre, prod.Prod_Descripcion, prod.Prod_Medida, prod.Prod_Precio, prod.Und_Id)

    try:
        cursor.execute(query, values)
        connection.commit()
        return { "message" : f"Producto {prod.Prod_Nombre} creado exitosamente!" }
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar producto {err}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de tipado al registrar producto {e}")
    finally:
        cursor.close()

## Update product
@router.put('/productos/{id}')
async def put_producto(id:int, prod : Producto) :
    cursor = connection.cursor()
    query = ("UPDATE Productos " 
             "SET Prod_Nombre = %s, " 
             "Prod_Descripcion = %s, "
             "Prod_Medida = %s, "
             "Prod_Precio = %s, "
             "Und_Id = %s "
             "WHERE Prod_Id = %s")
    values = (prod.Prod_Nombre, prod.Prod_Descripcion, prod.Prod_Medida, prod.Prod_Precio, prod.Und_Id, id)

    try:
        cursor.execute(query, tuple(values))
        connection.commit()
        return { "message" : f"Producto actualizado exitosamente!" }
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al actualizar producto {err}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de tipado al actualizar producto {e}")
    finally:
        cursor.close()

## Delete product
@router.delete('/productos/{id}')
async def delete_producto(id) :
    cursor = connection.cursor()
    query = "DELETE FROM Productos WHERE Prod_Id = %s"
    values = (id,)

    try:
        cursor.execute(query, values)
        connection.commit()
        return { "message" : f"Producto eliminado exitosamente!" }
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al eliminar producto {err}")
    except ValueError as e:
        raise HTTPException(status_code=403, detail=f"Error de tipado al eliminar producto {e}")
    finally:
        cursor.close()