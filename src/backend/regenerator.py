from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from base_model import BaseModel
from prompts import USER_INPUT_TEMPLATE, REGENERATOR_SYSTEM_PROMPT

TEMPERATURE = 0.8
MAX_OUTPUT_TOKENS = 250


class Regenerator(BaseModel):
    def __init__(self, local: bool = True):
        super().__init__(
            local=local, temperature=TEMPERATURE, max_tokens=MAX_OUTPUT_TOKENS
        )

        self.regenerator_prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", REGENERATOR_SYSTEM_PROMPT),
                ("human", USER_INPUT_TEMPLATE),
                ("ai", "{actor_output}"),
                ("human", "{critic_output}"),
            ]
        )

    def get_chain(self) -> Runnable:
        return self.regenerator_prompt_template | self.llm | self.parser
