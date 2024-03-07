from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def llm_sentence_emotion() -> LLMChain:
    prompt = PromptTemplate(
        input_variable=["sentence", "emotions"],
        template=Path("promppts_template/text_to_emotions.prompt".read_text())
    )
    llm = ChatOpenAI(temperate=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


def llm_lyrics_emotion() -> LLMChain:
    prompt = PromptTemplate(
        input_variable=["name", "lyrics", "emotions_used"],
        template=Path("promppts_template/lyrics_to_emotions.prompt".read_text())
    )
    llm = ChatOpenAI(temperate=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain