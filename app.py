import asyncio

from dependency import Dependency
from pricing_agent.agent import pricing_agent
from requirement_agent.agent import requirement_agent
from user_prompt import USER_PROMPT


async def main(user_prompt: str):

    req_result = await requirement_agent.run(user_prompt)
    tech_list = req_result.output.suggested_technologies

    pricing_prompt = f"Please provide a price breakdown for these technologies: {', '.join(tech_list)}"
    my_deps = Dependency(api_key="sk-your-fake-key-here")
    final_result = await pricing_agent.run(pricing_prompt, deps=my_deps)

    return final_result.output


if __name__ == "__main__":
    output = asyncio.run(main(user_prompt=USER_PROMPT))
    print(output)
