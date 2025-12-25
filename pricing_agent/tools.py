import random
from typing import Any, Dict, Tuple

from pydantic import BaseModel
from pydantic_ai import RunContext

from dependency import Dependency


class PricingDeps(BaseModel):
    api_key: str
    category_baselines: Dict[str, Tuple[int, int]] = {
        "frontend": (50, 200),
        "backend": (150, 500),
        "database": (100, 400),
        "cloud": (200, 1000),
        "security": (50, 150),
    }


async def get_service_cost(
    ctx: RunContext[Dependency],
    category: str,
    service_name: str,
    baselines: Dict[str, Tuple[int, int]],
) -> Dict[str, Any]:
    """Calculates a randomized market rate for a specific technical service.

    This function simulates a real-time pricing API call by generating a cost
    within a predefined range (baseline) for a given category. It ensures
    that service estimates are grounded in realistic financial bounds.

    Args:
        category: The technical domain (e.g., 'frontend', 'backend', 'database').
            Used to determine the appropriate price range from baselines.
        service_name: The specific technology or tool (e.g., 'React', 'PostgreSQL').
        baselines: A mapping of categories to their (min, max) price tuples.

    Returns:
        A dictionary containing:
            - service (str): The name of the technology.
            - category (str): The normalized (lowercase) category.
            - monthly_usd (float): The generated cost rounded to 2 decimal places.

    Example:
        >>> await get_service_cost("frontend", "React", {"frontend": (50, 100)})
        {'service': 'React', 'category': 'frontend', 'monthly_usd': 74.52}
    """
    if not ctx.deps.api_key:
        raise ValueError("API key is required to fetch service costs.")
    cat = category.lower()
    low, high = baselines.get(cat, (20, 100))

    cost = round(random.uniform(low, high), 2)

    return {
        "service": service_name,
        "category": cat,
        "monthly_usd": cost,
    }
