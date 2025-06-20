from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.handler import api_router
from app.handler.telegram import lifespan

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"/{settings.API_VERSION}/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_CORS_ORIGINS,
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix=f"/{settings.API_VERSION}")
