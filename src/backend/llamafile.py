from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


model = ChatOpenAI(model="LLaMA_CPP", base_url="http://127.0.0.1:8080/v1", temperature=0.5)
parser = StrOutputParser()
system_template = "You are an expert data generator. You are the best at creating unique, realistic data samples."
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

chain = prompt_template | model | parser

human_prompt = "Create a conversation between a call center technician and a customer who is having trouble with their internet connection."
print(chain.invoke({"text": human_prompt}))