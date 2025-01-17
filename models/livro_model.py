from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Livro(Base):
    # Modelo de dados para a tabela de livros
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    autor = Column(String)
    isbn = Column(String, unique=True, index=True)
    quantidade_disponivel = Column(Integer)
    categoria = Column(String)
    data_cadastro = Column(DateTime, default=datetime.utcnow) 

class Config:
    from_attributes = True 