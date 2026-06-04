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


def answer_question_about_document(text: str, question: str):

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are a document analysis assistant.

Only answer using information from the document.

If the answer is not in the document, say:
"The document does not contain enough information to answer this question."

Be clear and concise.
"""
            },
            {
                "role": "user",
                "content": f"""
Document:

{text}

Question:

{question}
"""
            }
        ]
    )

    return response.choices[0].message.content

def generate_embedding(text: str): 

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding