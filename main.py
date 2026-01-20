from fastapi import FastAPI
from typing import List, Optional
from uuid import UUID, uuid4
from fastapi import HTTPException
from uuid import UUID

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

@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return {"message": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/api/v1/user/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, user_update: Usuario):
    for index, user in enumerate(db):
        if user.id == user_id:
            user_update.id = user_id
            db[index] = user_update
            return user_update
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



@app.get("/api/v1/user/{user_id}", response_model=Usuario)
async def get_user_by_id(user_id: UUID):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
