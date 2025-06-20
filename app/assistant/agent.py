from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from app.assistant import prompt
from app.assistant.sub_agents.christian.agent import christian_agent
from app.assistant.sub_agents.general.agent import general_agent
from app.assistant.sub_agents.muslim.agent import muslim_agent
from app.assistant.sub_agents.philosopher.agent import philosopher_agent
from app.config import settings

omar = Agent(
    name="omar",
    model=LiteLlm(model=settings.OPENAI_MODEL),
    description="""
    A spiritual guide that uses specialized sub-agents to provide meaningful answers.
    """,
    instruction=prompt.OMAR_INSTRUCTION.strip(),
    sub_agents=[
        christian_agent,
        general_agent,
        muslim_agent,
        philosopher_agent,
    ],
)

# Set `omar` as the `root_agent`
root_agent = omar
