from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4

from model import Genero, Role, Usuario

app = FastAPI()

db: List[Usuario] = [
    Usuario(
        id=uuid4(),
        primerNombre="Jose Francisco",
        apellidos="Flores Amador",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        primerNombre="Luis Angel",
        apellidos="Flores Amador",
        genero=Genero.masculino,
        roles=[Role.user]
    )
]


@app.get("/")
async def root():
    return {"message": "Hola Mundo"}


@app.get("/api/v1/user")
async def get_user():
    return db
