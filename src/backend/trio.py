from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()


actor = ChatOpenAI(model="LLaMA_CPP", base_url="http://127.0.0.1:8080/v1", temperature=1.6, max_tokens=250)
critic = ChatOpenAI(model="LLaMA_CPP", base_url="http://127.0.0.1:8080/v1", temperature=0.9, max_tokens=300)
regenerator = ChatOpenAI(model="LLaMA_CPP", base_url="http://127.0.0.1:8080/v1", temperature=0.8, max_tokens=250)
# actor = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.6, max_tokens=250)
# critic = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9, max_tokens=150)
# regenerator = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8, max_tokens=250)

actor_system_prompt = "You are an expert data generator. You are the best at creating unique, realistic data samples. You must ONLY respond with the data sample and nothing else."
critic_system_prompt = "You are an expert data critic. Your task is to review the singular data sample and provide feedback on how it can be improved. Don't be afraid to be harsh."
regenerator_system_prompt = "You are an expert data regenerator. Your task is to take the original input, the original output, and the critic's feedback, and generate a refined data sample. You must ONLY respond with the refined data sample and nothing else. DO NOT change the topic or any essential information of the original input."

user_input_template = "Create a synthetic data sample representing a(n) {topic}. {few_shot}"

actor_prompt_template = ChatPromptTemplate.from_messages(
    [("system", actor_system_prompt), ("human", user_input_template)]
)
critic_prompt_template = ChatPromptTemplate.from_messages(
    [("system", critic_system_prompt), ("human", "This was the prompt:" + user_input_template + "and this is the generated data sample: {actor_output}")]
)
regenerator_prompt_template = ChatPromptTemplate.from_messages(
    [("system", regenerator_system_prompt), ("human", user_input_template), ("ai", "{actor_output}"), ("human", "{critic_output}")]
)

parser = StrOutputParser()


actor_chain = actor_prompt_template | actor | parser
critic_chain = critic_prompt_template | critic | parser
regenerator_chain = regenerator_prompt_template | regenerator | parser

def invoke_full_chain(topic, few_shot_examples=[]):
    few_shot_string = "\n---\n".join(few_shot_examples)
    few_shot_template = f"Here are some examples of what I want the data sample to look like: {few_shot_string}. These are just a guide and you can use them as inspiration for your response."

    input = {"topic": topic, "few_shot": few_shot_template if few_shot_examples else ""}
    actor_output = actor_chain.invoke(input)
    print(f"actor_output: \n{actor_output}\n\n")
    print("-" * 50)

    input["actor_output"] = actor_output
    critic_output = critic_chain.invoke(input)
    print(f"critic_output: \n{critic_output}\n\n")
    print("-" * 50)

    input["critic_output"] = critic_output
    final_output = regenerator_chain.invoke(input)
    return final_output

#chain = actor_prompt_template | actor | critic_prompt_template | critic | regenerator_prompt_template | regenerator | parser

topic = "amazon product review"
few_shot_examples = ["This speaker absolutely sucks. The battery only lasts for around an hour and it didnt come charged. So overpriced",
                     "These are the best towels ever. Super soft but don't leave lint everywhere. I love them!"
]

print(invoke_full_chain(topic, few_shot_examples))
