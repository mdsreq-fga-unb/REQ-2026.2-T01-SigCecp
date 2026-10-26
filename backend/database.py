
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as variáveis do arquivo .env
load_dotenv(BASE_DIR / ".env")

# URL do banco de dados
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{BASE_DIR / 'sigcecp.db'}",
)

# SQLite precisa dessa opção para funcionar com FastAPI
# em diferentes threads.
connect_args = {}

if DATABASE_URL.startswith("sqlite"):
    connect_args["check_same_thread"] = False

# Cria a conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=False,
)

# Fábrica de sessões para consultas e transações
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# Classe-base para os modelos do banco
class Base(DeclarativeBase):
    pass


# Dependência para disponibilizar uma sessão por requisição
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
