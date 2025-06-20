from contextlib import asynccontextmanager

from fastapi import FastAPI
from telegram import Message, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from app.config import settings

# Initialize the Telegram 🤖 application with configured settings
TELEGRAM = (
    ApplicationBuilder()
    .token(settings.TELEGRAM_TOKEN)
    .read_timeout(settings.TELEGRAM_READ_TIMEOUT)
    .get_updates_read_timeout(settings.TELEGRAM_READ_TIMEOUT)
    .build()
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    FastAPI lifespan context manager to handle Telegram bot startup and shutdown.
    """
    await TELEGRAM.bot.setWebhook(settings.WEBHOOK_URL)
    async with TELEGRAM:
        await TELEGRAM.start()
        yield
        await TELEGRAM.stop()


async def ask(update: Update, _: ContextTypes.DEFAULT_TYPE) -> Message | None:
    """
    Handler for user questions or spiritual inquiries.
    """
    raise NotImplementedError  # This is where Omar would listen and respond


async def help(update: Update, _: ContextTypes.DEFAULT_TYPE) -> Message | None:
    """
    Sends a help message with available commands and guidance.
    """
    # fmt: off
    if (reply := update.message.reply_text if update.message else None):
    # fmt: on
        await reply(settings.TELEGRAM_HELP_COMMAND)


async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> Message | None:
    """
    Welcomes the user and introduces Omar as a spiritual companion.
    """
    greetings = f"Hey {update.message.chat.first_name}" if update.message else "Hey"

    # fmt: off
    if (reply := update.message.reply_text if update.message else None):
    # fmt: on
        await reply(
            f"{greetings},\n\nPeace be upon you. I'm Omar, your spiritual companion. " \
            + "Whatever's on your heart or mind, I'm here. Ask away."
        )


# Register Omar's ears and voice:
# - /start welcomes the user
# - /help offers gentle guidance
# - All other text is treated as a heartfelt question
TELEGRAM.add_handler(CommandHandler("help", help))
TELEGRAM.add_handler(CommandHandler("start", start))
TELEGRAM.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ask))
