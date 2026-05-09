from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY, GROQ_MODEL_NAME

itinerary_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        (
            "You are a helpful travel assistant. Create a concise day trip itinerary "
            "for {city} based on these interests: {interests}. Return a brief bulleted list."
        ),
    ),
    ("human", "Create my day trip itinerary."),
])

FALLBACK_MODEL_NAME = "llama-3.1-8b-instant"


def _get_llm(model_name: str) -> ChatGroq:
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=model_name,
        temperature=0.3,
    )


def _should_retry_with_smaller_model(exc: Exception) -> bool:
    message = str(exc).lower()
    return "413" in message or "request_too_large" in message or "request entity too large" in message

def generate_itineary(city:str , interests:list[str]) -> str:
    formatted_interests = ", ".join(interest.strip() for interest in interests if interest.strip())
    prompt_messages = itinerary_prompt.format_messages(city=city, interests=formatted_interests)

    model_candidates = [GROQ_MODEL_NAME]
    if FALLBACK_MODEL_NAME not in model_candidates:
        model_candidates.append(FALLBACK_MODEL_NAME)

    last_error = None
    for model_name in model_candidates:
        try:
            response = _get_llm(model_name).invoke(prompt_messages)
            return response.content
        except Exception as exc:
            last_error = exc
            if model_name == model_candidates[-1] or not _should_retry_with_smaller_model(exc):
                raise

    raise last_error