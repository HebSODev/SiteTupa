from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from schemas.livro_schema import LivroCreate, LivroResponse
from models.livro_model import Livro
from database.database import get_db

router = APIRouter(prefix="/livros", tags=["livros"])

@router.post("/", response_model=LivroResponse)
async def criar_livro(livro: LivroCreate, db: Session = Depends(get_db)):
    db_livro = Livro(
        titulo=livro.titulo,
        autor=livro.autor,
        isbn=livro.isbn,
        quantidade_disponivel=livro.quantidade_disponivel,
        categoria=livro.categoria
    )
    db.add(db_livro)
    db.commit()
    db.refresh(db_livro)
    return db_livro

@router.get("/{livro_id}", response_model=LivroResponse)
async def obter_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@router.get("/", response_model=List[LivroResponse])
async def listar_livros(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    livros = db.query(Livro).offset(skip).limit(limit).all()
    return livros

@router.put("/{livro_id}", response_model=LivroResponse)
async def atualizar_livro(livro_id: int, livro: LivroCreate, db: Session = Depends(get_db)):
    db_livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    for key, value in livro.dict().items():
        setattr(db_livro, key, value)
    
    db.commit()
    db.refresh(db_livro)
    return db_livro

@router.delete("/{livro_id}")
async def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    db_livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if db_livro is None:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    
    db.delete(db_livro)
    db.commit()
    return {"message": "Livro deletado com sucesso"} 