import asyncio

from dependency import Dependency
from pricing_agent.agent import pricing_agent
from requirement_agent.agent import requirement_agent
from sysdesign_agent.agent import sysdesign_agent
from user_prompt import USER_PROMPT


async def main(user_prompt: str):

    req_result = await requirement_agent.run(user_prompt)
    tech_list = req_result.output.suggested_technologies

    components_str = {", ".join(tech_list)}
    pricing_prompt = (
        f"Provide a price breakdown for this architecture: {components_str}"
    )
    my_deps = Dependency(api_key="sk-your-fake-key-here")
    pricing_result = await pricing_agent.run(pricing_prompt, deps=my_deps)

    design_prompt = f"Design a system architecture using these technologies: {', '.join(pricing_result)}"
    final_result = await sysdesign_agent.run(design_prompt)

    return final_result.output


if __name__ == "__main__":
    output = asyncio.run(main(user_prompt=USER_PROMPT))
    print(output)
