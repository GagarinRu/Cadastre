from fastapi import FastAPI
from sqladmin import Admin

from app.api.routers import main_router
from app.core.config import settings
from app.core.db import engine
from app.models import CadastreAdmin

app = FastAPI(
    title=settings.app_title,
)

app.include_router(main_router)


admin = Admin(app, engine)
admin.add_view(CadastreAdmin)
