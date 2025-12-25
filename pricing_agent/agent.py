from typing import List

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from ai_model import model
from pricing_agent.prompt import PRICING_AGENT_PROMPT
from pricing_agent.tools import get_service_cost


class ServicePrice(BaseModel):
    service: str = Field(description="Name of the technology or tool")
    category: str = Field(description="The domain (frontend, backend, etc.)")
    price: float = Field(description="The monthly cost in USD")


# 2. Define the final output (The Contract)
class PricingAgentOutput(BaseModel):
    found: bool = Field(description="True if pricing was successfully retrieved")
    breakdown: List[ServicePrice] = Field(
        description="A granular list of each component's cost"
    )
    total_cost: float = Field(description="The sum of all prices in the breakdown")


pricing_agent = Agent(
    model=model,
    system_prompt=PRICING_AGENT_PROMPT,
    output_type=PricingAgentOutput,
    retries=2,
)


pricing_agent.tool(get_service_cost)
