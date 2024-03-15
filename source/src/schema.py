from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Client(Base):
    __tablename__ = "Clients"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    endereco = Column(String)
    telefone = Column(Integer)

    def __repr__(self):
        return f"User: {self.nome}"
