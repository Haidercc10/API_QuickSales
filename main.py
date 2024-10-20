from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import routers.usuarios
import routers.productos
import routers.roles

app = FastAPI()
app.include_router(routers.usuarios.router)
app.include_router(routers.productos.router)
app.include_router(routers.roles.router)

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





