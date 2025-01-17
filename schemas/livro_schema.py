from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class LivroBase(BaseModel):
    titulo: str
    autor: str
    isbn: str
    quantidade_disponivel: int
    categoria: str

class LivroCreate(LivroBase):
    # Schema para criação de livro
    @validator('isbn')
    def validar_isbn(cls, v):
        # Validação básica de ISBN (13 dígitos)
        if not v.isdigit() or len(v) != 13:
            raise ValueError('ISBN deve conter 13 dígitos numéricos')
        return v

class LivroResponse(LivroBase):
    # Schema para resposta de livro
    id: int
    data_cadastro: datetime

    class Config:
        orm_mode = True 