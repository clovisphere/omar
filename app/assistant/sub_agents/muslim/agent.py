from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from app.assistant.sub_agents.muslim import prompt
from app.config import settings

muslim_agent = Agent(
    name="muslim_agent",
    model=LiteLlm(model=settings.OPENAI_MODEL),
    description="""
    Responds to questions grounded in Islamic scripture, practice, and theology.
    """,
    instruction=prompt.MUSLIM_AGENT_INSTRUCTION.strip(),
)
