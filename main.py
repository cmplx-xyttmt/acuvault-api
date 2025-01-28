from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from acu_collections.routes import router as collections_router


def get_application():
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    _app.include_router(collections_router, prefix="/api/v1/acu_collections", tags=["acu_collections"])

    return _app


app = get_application()
