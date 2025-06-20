from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.assistant.agent import root_agent
from app.config import settings

# 🌱 Persistent session management for ephemeral chats
session_service = InMemorySessionService()

# 🧠 Initialize the Runner — this will orchestrate message exchange with Omar
runner = Runner(
    agent=root_agent,
    app_name=settings.PROJECT_NAME,
    session_service=session_service,
)


async def call_agent_async(query: str, user_id: str, session_id: str) -> str:
    """Sends a query to Omar and retrieves the final response."""
    # 🧾 Attempt to retrieve existing session
    if not (
        await session_service.get_session(
            app_name=settings.PROJECT_NAME,
            user_id=user_id,
            session_id=session_id,
        )
    ):
        # ✨ If none exists, create a new spiritual channel
        await session_service.create_session(
            app_name=settings.PROJECT_NAME,
            user_id=user_id,
            session_id=session_id,
        )

    # 🗣️ Build the message payload for the agent
    content = types.Content(role="user", parts=[types.Part(text=query)])

    # 🧠 Omar channels the message and listens for the final answer
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=content
    ):
        if (
            event.is_final_response()
            and event.content
            and event.content.parts
            and event.content.parts[0].text
        ):
            return event.content.parts[0].text

    # 🕊️ If no answer, return a gentle fallback
    return "🙏 Sorry, I couldn't find a response to that right now."
