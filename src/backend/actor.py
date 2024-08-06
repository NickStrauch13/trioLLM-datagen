from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from base_model import BaseModel
from prompts import USER_INPUT_TEMPLATE, ACTOR_SYSTEM_PROMPT

TEMPERATURE = 1.6
MAX_OUTPUT_TOKENS = 250


class Actor(BaseModel):
    def __init__(self, local: bool = True):
        super().__init__(
            local=local, temperature=TEMPERATURE, max_tokens=MAX_OUTPUT_TOKENS
        )

        self.actor_prompt_template = ChatPromptTemplate.from_messages(
            [("system", ACTOR_SYSTEM_PROMPT), ("human", USER_INPUT_TEMPLATE)]
        )

    def get_chain(self) -> Runnable:
        return self.actor_prompt_template | self.llm | self.parser
