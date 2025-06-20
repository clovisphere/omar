import asyncio
import uuid
import warnings

import click
from art import tprint  # type: ignore

from app.assistant.helper import call_agent_async
from app.config import settings

# Ignore all warnings
warnings.filterwarnings("ignore")

# Generate a unique identifier for the user (simulating a new visitor every time)
user_id = f"user_{uuid.uuid4()}"
# Generate a unique identifier for this particular session (a unique chat instance)
session_id = f"session_{uuid.uuid4()}"


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
        )
    )


async def chat(user_id: str, session_id: str) -> None:
    """Handles the chat interaction loop with the user."""
    click.secho(
        "\nPeace be upon you. I'm Omar, your spiritual companion. "
        + "Whatever's on your heart or mind, I'm here. Ask away",
        fg="blue",
    )
    click.secho("Type 'quit' or 'q' to exit the chat.\n", fg="magenta")

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

        # 📡 Send the user question to Omar and await a sacred reply
        response = await call_agent_async(question, user_id, session_id)

        # ✨ Display the response to the user
        click.secho(f"> {response}", fg="bright_cyan")


# Run the CLI
if __name__ == "__main__":
    console()
