from openai import OpenAI
from utils.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_ai_summary(text: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You summarize documents clearly and concisely."
            },
            {
                "role": "user",
                "content": f"Summarize this text:\n\n{text}"
            }
        ]
    )

    return response.choices[0].message.content