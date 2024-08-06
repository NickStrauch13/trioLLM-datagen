import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/backend"))
)
from prompts import *


def test_prompts():
    """
    Verify that the prompt attributes are valid.
    """
    assert isinstance(USER_INPUT_TEMPLATE, str)
    assert isinstance(FEW_SHOT_TEMPLATE, str)
    assert isinstance(ACTOR_SYSTEM_PROMPT, str)
    assert isinstance(CRITIC_SYSTEM_PROMPT, str)
    assert isinstance(CRITIC_HUMAN_TEMPLATE, str)
    assert isinstance(REGENERATOR_SYSTEM_PROMPT, str)
