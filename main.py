from fastapi import FastAPI
from routers import livro_routes
from database.database import engine
from models.livro_model import Base

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="Biblioteca API",
    description="API para gerenciamento de biblioteca",
    version="1.0.0"
)

# Inclusão das rotas
app.include_router(livro_routes.router, prefix="/api/v1") 