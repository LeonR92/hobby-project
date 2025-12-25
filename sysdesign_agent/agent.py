from typing import List

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from ai_model import model
from sysdesign_agent.prompt import SYSTEM_DESIGN_AGENT_PROMPT


class SystemComponent(BaseModel):
    name: str = Field(description="Name of the component (e.g., 'Redis Cache')")
    role: str = Field(description="The specific responsibility in the architecture")
    justification: str = Field(
        description="Why this component is necessary for SOTA design"
    )


class SysdesignAgentOutput(BaseModel):
    architecture_summary: str = Field(
        description="High-level summary of the architectural pattern (e.g., Microservices, Event-driven)"
    )
    architecture_diagram_url: str = Field(
        description="A Mermaid.js or URL link to the visual representation"
    )
    components: List[SystemComponent] = Field(
        description="Deep dive into each major architectural block"
    )
    bottlenecks: List[str] = Field(
        description="Potential scaling issues or single points of failure identified"
    )


sysdesign_agent = Agent(
    model=model,
    system_prompt=SYSTEM_DESIGN_AGENT_PROMPT,
    output_type=SysdesignAgentOutput,
    retries=3,
)
