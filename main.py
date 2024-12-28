# the main code to run the agent

from openai import OpenAI
import os
from dotenv import load_dotenv

# let's load the key api key for the openai
load_dotenv()
# let's update the base url to forward traffic to out model
openai_base_url = os.getenv("OPENAI_BASE_URL")
# let's define the openai client 
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_says(
    messages, model="gpt-3.5-turbo", max_tokens=100
):
    """Generates text with conversation."""
    return openai_client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
    )

