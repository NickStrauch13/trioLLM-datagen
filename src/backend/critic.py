from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from base_model import BaseModel
from prompts import CRITIC_SYSTEM_PROMPT, CRITIC_HUMAN_TEMPLATE, USER_INPUT_TEMPLATE

TEMPERATURE = 0.9
MAX_OUTPUT_TOKENS = 300


class Critic(BaseModel):
    def __init__(self, local: bool = True):
        super().__init__(
            local=local, temperature=TEMPERATURE, max_tokens=MAX_OUTPUT_TOKENS
        )

        self.critic_prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", CRITIC_SYSTEM_PROMPT),
                (
                    "human",
                    CRITIC_HUMAN_TEMPLATE.format(
                        user_input=USER_INPUT_TEMPLATE, actor_output="{actor_output}"
                    ),
                ),
            ]
        )

    def get_chain(self) -> Runnable:
        return self.critic_prompt_template | self.llm | self.parser
