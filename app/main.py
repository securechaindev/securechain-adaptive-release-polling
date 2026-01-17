from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.database import DatabaseManager
from app.exception_handler import ExceptionHandler
from app.middleware import LogRequestMiddleware
from app.router import api_router
from app.settings import settings

DESCRIPTION = """
This repo is in progress.
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager = DatabaseManager()
    await db_manager.initialize()
    yield
    await db_manager.close()

app = FastAPI(
    title="Secure Chain Adaptive Release Polling Tool",
    docs_url=settings.DOCS_URL,
    version="0.1.0",
    description=DESCRIPTION,
    contact={
        "name": "Secure Chain Team",
        "url": "https://github.com/securechaindev",
        "email": "hi@securechain.dev",
    },
    license_info={
        "name": "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
    lifespan=lifespan
)

app.add_middleware(LogRequestMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.SERVICES_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(RequestValidationError, ExceptionHandler.request_validation_exception_handler)
app.add_exception_handler(HTTPException, ExceptionHandler.http_exception_handler)
app.add_exception_handler(Exception, ExceptionHandler.unhandled_exception_handler)


app.include_router(api_router)
