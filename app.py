import asyncio

from dependency import Dependency
from pricing_agent.agent import pricing_agent
from requirement_agent.agent import requirement_agent
from sysdesign_agent.agent import sysdesign_agent
from user_prompt import USER_PROMPT
from utils import generate_markdown_report


async def main(user_prompt: str):
    req_result = await requirement_agent.run(user_prompt)
    tech_list = req_result.output.suggested_technologies
    design_prompt = (
        f"Design a system architecture using these technologies: {', '.join(tech_list)}"
    )
    design_result = await sysdesign_agent.run(design_prompt)

    component_names = [c.name for c in design_result.output.components]

    pricing_prompt = f"Provide a price breakdown for this specific architecture: {', '.join(component_names)}"
    my_deps = Dependency(api_key="sk-your-fake-key-here")
    pricing_result = await pricing_agent.run(pricing_prompt, deps=my_deps)

    return {"design": design_result.output, "pricing": pricing_result.output}


if __name__ == "__main__":
    output = asyncio.run(main(user_prompt=USER_PROMPT))
    markdown_content = generate_markdown_report(output["design"], output["pricing"])
    with open("system_report.md", "w") as f:
        f.write(markdown_content)
    print(output)
