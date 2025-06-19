from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from app.assistant.sub_agents.christian import prompt
from app.config import settings

christian_agent = Agent(
    name="christian_agent",
    model=LiteLlm(model=settings.OPENAI_MODEL),
    description="""
    Answers questions about Christian teachings, scripture, and theology.
    """,
    instruction=prompt.CHRISTIAN_AGENT_INSTRUCTION.strip(),
)
