from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .config import session
from .schema import Client
from .model import Model

api_router = APIRouter()


@api_router.get("/api/users")
async def getUsers():
    content = {}
    query = session.query(Client).all()
    for client in query:
        content[client.id] = {"id": client.id,
                              "nome": client.nome,
                              "idade": client.idade,
                              "email": client.email,
                              "endereco": client.endereco,
                              "telefone": client.telefone}
    return JSONResponse(content=content)


@api_router.get("/api/users/{id}")
async def getUsers(id: int):
    content = {}
    info = session.query(Client).filter_by(id=id).first()
    if info:
        content["User"] = {"id": info.id,
                           "nome": info.nome,
                           "idade": info.idade,
                           "email": info.email,
                           "endereco": info.endereco,
                           "telefone": info.telefone}
    else:
        return JSONResponse(content={"message": f"Client with ID {id} not found!"})
    return JSONResponse(content=content)


@api_router.post("/api/create")
async def createUser(client: Model):
    client = Client(id=None, nome=client.nome, idade=client.idade, email=client.email,
                    endereco=client.endereco, telefone=client.telefone)
    try:
        if session.add(client):
            session.commit()
    except Exception as err:
        return JSONResponse(content={"error_message": err, "error_type": type(err).__name__})


@api_router.put("/api/update/{id}")
async def updateUser(id: int, client: Model):
    info = session.query(Client).filter_by(id=id).first()
    if info:
        info.nome = client.nome if client.nome != "string" else info.nome
        info.idade = client.idade if client.idade > 0 else info.idade
        info.email = client.email if client.email != "string" else info.email
        info.endereco = client.endereco if client.endereco != "string" else info.endereco
        info.telefone = client.telefone if client.telefone != 0 else info.telefone
    else:
        return JSONResponse(content={"message": f"Client with ID {id} not found!"})
