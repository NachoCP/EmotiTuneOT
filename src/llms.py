from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def llm_sentence_emotion() -> LLMChain:
    print(Path("prompts_template/text_to_emotions.prompt").read_text())
    prompt = PromptTemplate(
        input_variables=["sentence"],
        template=Path("prompts_template/text_to_emotions.prompt").read_text(),
    )

    llm = ChatOpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain


def llm_lyrics_emotion() -> LLMChain:
    prompt = PromptTemplate(
        input_variables=["name", "lyrics", "emotions_used"],
        template=Path("prompts_template/lyrics_to_emotions.prompt").read_text())

    llm = ChatOpenAI(temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain