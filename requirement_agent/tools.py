from pydantic_ai import RunContext


async def generate_technical_specs(ctx: RunContext[None], user_features: str) -> str:
    """
    Translates raw user features into technical specifications.
    Use this tool to break down complexity before finalizing the report.
    """
    return f"Technical Spec breakdown for: {user_features}"
