from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from app.assistant.sub_agents.general import prompt
from app.config import settings

general_agent = Agent(
    name="general_agent",
    model=LiteLlm(model=settings.OPENAI_MODEL),
    description="""
    Provides spiritual and philosophical guidance beyond specific traditions.
    """,
    instruction=prompt.GENERAL_AGENT_INSTRUCTION.strip(),
)
