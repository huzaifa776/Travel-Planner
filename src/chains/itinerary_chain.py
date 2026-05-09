from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY, GROQ_MODEL_NAME

itnineary_prompt = ChatPromptTemplate([
    ("system" , "You are a helpful travel asssistant. Create a day trip itineary for {city} based on user's interest : {interests}. Provide a brief , bulleted itineary"),
    ("human" , "Create a itineary for my day trip")
])


def _get_llm() -> ChatGroq:
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL_NAME,
        temperature=0.3,
    )

def generate_itineary(city:str , interests:list[str]) -> str:
    llm = _get_llm()
    response = llm.invoke(
        itnineary_prompt.format_messages(city=city,interests=', '.join(interests))
    )

    return response.content