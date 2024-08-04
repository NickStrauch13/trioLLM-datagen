import os
import sys
from langchain_core.runnables import Runnable
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/backend')))
from base_model import BaseModel
from actor import Actor
from critic import Critic
from regenerator import Regenerator
from llm_trio import LLMTrio


def test_actor():
    """
    Test the Actor class.
    Verify that the class is an instance of BaseModel and that the get_chain method returns a Runnable.
    Also verify that the prompt, llm, and parser attributes are created successfully.
    """
    actor = Actor(local=True)
    chain = actor.get_chain()
    assert isinstance(actor, BaseModel)
    assert isinstance(chain, Runnable)
    assert isinstance(actor.actor_prompt_template, ChatPromptTemplate)
    assert isinstance(actor.llm, ChatOpenAI)
    assert isinstance(actor.parser, StrOutputParser)


def test_critic():
    """
    Test the Critic class.
    Verify that the class is an instance of BaseModel and that the get_chain method returns a Runnable.
    Also verify that the prompt, llm, and parser attributes are created successfully.
    """
    critic = Critic(local=True)
    chain = critic.get_chain()
    assert isinstance(critic, BaseModel)
    assert isinstance(chain, Runnable)
    assert isinstance(critic.critic_prompt_template, ChatPromptTemplate)
    assert isinstance(critic.llm, ChatOpenAI)
    assert isinstance(critic.parser, StrOutputParser)


def test_regenerator():
    """
    Test the Regenerator class.
    Verify that the class is an instance of BaseModel and that the get_chain method returns a Runnable.
    Also verify that the prompt, llm, and parser attributes are created successfully.
    """
    regenerator = Regenerator(local=True)
    chain = regenerator.get_chain()
    assert isinstance(regenerator, BaseModel)
    assert isinstance(chain, Runnable)
    assert isinstance(regenerator.regenerator_prompt_template, ChatPromptTemplate)
    assert isinstance(regenerator.llm, ChatOpenAI)
    assert isinstance(regenerator.parser, StrOutputParser)


def test_llm_trio():
    """
    Test the LLMTrio class.
    Verify that all submodels are working together as expected.
    """
    trio = LLMTrio()
    trio_actor = trio.actor_chain
    trio_critic = trio.critic_chain
    trio_regenerator = trio.regenerator_chain
    assert isinstance(trio_actor, Runnable)
    assert isinstance(trio_critic, Runnable)
    assert isinstance(trio_regenerator, Runnable)
