import asyncio
import uuid
import warnings

import click
from art import tprint  # type: ignore
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.assistant.agent import root_agent
from app.config import settings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Create an in-memory session service to manage user sessions temporarily
session_service = InMemorySessionService()
# Generate a unique identifier for the user (simulating a new visitor every time)
user_id = f"user_{uuid.uuid4()}"
# Generate a unique identifier for this particular session (a unique chat instance)
session_id = f"session_{uuid.uuid4()}"


async def call_agent_async(
    query: str, user_id: str, session_id: str, runner: Runner
) -> str | None:
    """Sends a query to Omar and retrieves the final response."""
    content = types.Content(role="user", parts=[types.Part(text=query)])
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

    return "🙏 Sorry, I couldn't find a response to that right now."


@click.command()
def console() -> None:
    """Entry point for the Omar CLI."""
    click.echo(tprint(f"{settings.PROJECT_NAME}", font="tarty7"))
    click.secho("🌿 Starting interactive chat...\n", fg="green")

    # Run the asynchronous chat loop with the generated identifiers and session handler
    asyncio.run(
        chat(
            user_id=user_id,
            session_id=session_id,
            session_service=session_service,
        )
    )


async def chat(
    user_id: str, session_id: str, session_service: InMemorySessionService
) -> None:
    """Handles the chat interaction loop with the user."""
    click.secho(
        "\nPeace be upon you. I'm Omar, your spiritual companion. "
        + "Whatever's on your heart or mind, I'm here. Ask away",
        fg="blue",
    )
    click.secho("Type 'quit' or 'q' to exit the chat.\n", fg="magenta")

    # 🛖 Create a new session space for this chat instance
    await session_service.create_session(
        app_name=settings.PROJECT_NAME,
        user_id=user_id,
        session_id=session_id,
    )

    # 🧠 Initialize the Runner — this will orchestrate message exchange with Preacher
    runner = Runner(
        agent=root_agent,
        app_name=settings.PROJECT_NAME,
        session_service=session_service,
    )

    # 🔁 Begin the chat loop — our little chapel of conversation
    while True:
        question = input("You: ").strip()

        # 🛑 Exit the loop if the user wants to end the session
        if question.lower() in {"quit", "q"}:
            click.secho("🙏 Until next time. Walk in peace.", fg="red")
            break

        # ⚠️ Remind the user to ask something meaningful
        if not question:
            click.secho("⚠️ Please enter a question to continue.", fg="yellow")
            continue

        # 📡 Send the user question to Preacher and await a sacred reply
        response = await call_agent_async(question, user_id, session_id, runner)

        # ✨ Display the response to the user
        click.secho(f"> {response}", fg="bright_cyan")


# Run the CLI
if __name__ == "__main__":
    console()
