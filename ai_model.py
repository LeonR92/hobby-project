import os

from dotenv import load_dotenv
from pydantic_ai.models.mistral import MistralModel

AI_MODEL = "ministral-14b-latest"


load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")


model = MistralModel(AI_MODEL)
