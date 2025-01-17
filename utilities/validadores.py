from fastapi import HTTPException
from models.livro_model import Livro

async def verificar_isbn_duplicado(isbn: str, session) -> bool:
  
    # Verifica se existe algum livro com o ISBN informado
    livro_existente = await session.query(Livro).filter(Livro.isbn == isbn).first()
    
    if livro_existente:
        raise HTTPException(
            status_code=400,
            detail=f"Já existe um livro cadastrado com o ISBN {isbn}"
        )
    
    return False 