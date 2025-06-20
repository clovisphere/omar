from fastapi import APIRouter, Request, status
from telegram import Update

from app.handler.telegram import TELEGRAM
from app.logger import log

router = APIRouter()


@router.post(
    "/webhook",
    description="The webhook used by telegram to send request",
    status_code=status.HTTP_200_OK,
)
async def process(request: Request):
    req = await request.json()

    log.debug("Received a request from Telegram via webhook 😉...", req=req)

    await TELEGRAM.process_update(update=Update.de_json(req, TELEGRAM.bot))
    # No return required. FastAPI will automatically return 200 OK with an empty body.
