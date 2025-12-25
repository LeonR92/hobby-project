from typing import ClassVar, List

from pydantic import BaseModel, Field, field_validator
from pydantic_ai import Agent

from ai_model import model
from requirement_agent.prompt import REQUIREMENT_AGENT_PROMPT
from requirement_agent.tools import generate_technical_specs


class RequirementAgentOutput(BaseModel):
    requirements_summary: str = Field(
        description="Executive summary of the technical needs"
    )
    suggested_technologies: List[str] = Field(description="List of stack components")
    cost_estimate: float = Field(description="Total project cost in USD")

    MINIMUM_COST: ClassVar[float] = 500.0

    @field_validator("cost_estimate")
    @classmethod
    def validate_cost(
        cls,
        v: float,
    ) -> float:
        if v < cls.MINIMUM_COST:
            raise ValueError(
                f"Estimate of ${v} is too low. Minimum infrastructure "
                "baseline is $500. Please re-calculate including hosting."
            )
        return v


requirement_agent = Agent(
    model=model,
    system_prompt=REQUIREMENT_AGENT_PROMPT,
    output_type=RequirementAgentOutput,
    retries=2,
)


requirement_agent.tool_plain(generate_technical_specs)
