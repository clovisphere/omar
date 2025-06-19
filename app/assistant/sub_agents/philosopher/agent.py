from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from app.assistant.sub_agents.philosopher import prompt
from app.config import settings

philosopher_agent = Agent(
    name="philosopher_agent",
    model=LiteLlm(model=settings.OPENAI_MODEL),
    description="""
    Explores life's big questions using philosophical reasoning from diverse traditions.
    """,
    instruction=prompt.PHILOSOPHER_AGENT_INSTRUCTION.strip(),
)
