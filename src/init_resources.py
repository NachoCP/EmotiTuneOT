import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv
load_dotenv()

from src.llms import llm_sentence_emotion
from src.vector_db import load_db
from src.constants import DATASET_NAME
from src.constants import EMBEDDING_MODEL

@st.cache_resource
def init_resources():
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    dataset_path = f"hub://{os.environ['ACTIVELOOP_ORG_ID']}/{DATASET_NAME}"
    chain = llm_sentence_emotion()
    db = load_db(dataset_path=dataset_path,
                 embedding=embeddings)

    return db, chain