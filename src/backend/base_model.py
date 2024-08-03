from abc import ABC, abstractmethod
import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable


PROPRIETARY_MODEL = "gpt-4o-mini"
LOCAL_MODEL = "LLaMA_CPP"
BASE_URL = os.getenv('LLM_ENDPOINT_URL')
if not BASE_URL:
  BASE_URL = "http://127.0.0.1:8080/v1"


class BaseModel(ABC):
  def __init__(self, local: bool = True, temperature: float = 1, max_tokens: int = 250):
    model = LOCAL_MODEL if local else PROPRIETARY_MODEL
    base_url = BASE_URL if local else None
    self.llm = ChatOpenAI(model=model, 
                            base_url=base_url, 
                            temperature=temperature, 
                            max_tokens=max_tokens)
    self.parser = StrOutputParser()

  @abstractmethod
  def get_chain(self) -> Runnable:
    pass
