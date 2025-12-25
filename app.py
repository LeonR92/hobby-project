import asyncio

from requirement_agent.agent import requirement_agent
from user_prompt import USER_PROMPT


async def main(user_prompt: str):
    result = await requirement_agent.run(user_prompt)
    return result.output


if __name__ == "__main__":
    output = asyncio.run(main(user_prompt=USER_PROMPT))
    print(output)
