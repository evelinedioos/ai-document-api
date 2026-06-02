from services.openai_service import generate_ai_summary

def generate_summary(text: str):
    summary = generate_ai_summary(text)
    return summary