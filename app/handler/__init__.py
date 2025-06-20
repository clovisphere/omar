from fastapi import APIRouter

from app.handler import webhook

api_router = APIRouter()

api_router.include_router(webhook.router, tags=["Omar's Telegram Webhook"])
