from services.openai_service import answer_question_about_document


def ask_question(text: str, question: str):
    return answer_question_about_document(text, question)