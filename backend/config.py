from pathlib import Path
from fastapi.templating import Jinja2Templates
from backend.auth.csrf import contexto_csrf

BASE_DIR = Path(__file__).resolve().parent.parent

FRONTEND_DIR = BASE_DIR / "frontend"
ASSETS_DIR = FRONTEND_DIR / "assets"

templates = Jinja2Templates(directory=FRONTEND_DIR, context_processors=[contexto_csrf])