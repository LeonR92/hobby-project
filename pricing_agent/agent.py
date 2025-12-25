from typing import List

from pydantic import BaseModel, Field, computed_field
from pydantic_ai import Agent

from ai_model import model
from pricing_agent.prompt import PRICING_AGENT_PROMPT
from pricing_agent.tools import get_service_cost


class ServicePrice(BaseModel):
    service: str = Field(description="Name of the technology or tool")
    category: str = Field(description="The domain (frontend, backend, etc.)")
    price: float = Field(description="The monthly cost in USD")


class PricingAgentOutput(BaseModel):
    found: bool = Field(description="True if pricing was successfully retrieved")
    breakdown: List[ServicePrice] = Field(
        description="A granular list of each component's cost"
    )

    @computed_field
    @property
    def total_cost(self) -> float:
        """Deterministically sums the breakdown. The LLM never touches this."""
        return round(sum(item.price for item in self.breakdown), 2)


pricing_agent = Agent(
    model=model,
    system_prompt=PRICING_AGENT_PROMPT,
    output_type=PricingAgentOutput,
    retries=2,
)


pricing_agent.tool(get_service_cost)
