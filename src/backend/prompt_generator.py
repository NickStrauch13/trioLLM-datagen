"""
Functions to generate prompts for each of the unique LLMs.
"""


def generate_prompt_expansion_prompt(user_input: str) -> str:
    """
    Generate a prompt for the expansion LLM.

    Args:
        user_input (str): The user's input.

    Returns:
        str: The expanded prompt.
    """
    system_prompt = '''
                    You are a language model specialized in expanding concise user input prompts into detailed, 
                    contextually rich instructions for generating synthetic text data. Your goal is to create 
                    instructions that help another model generate high-quality synthetic data for fine-tuning tasks. 

                    Examples: 

                    Input Prompt: "Product reviews for electronic devices."
                    Expanded Prompt: "Generate a detailed product review for an electronic device. Highlight specific features and user experiences, detailing either positive or negative points. Pick a tone and style, such as enthusiastic, critical, or analytical."

                    Input Prompt: "Customer conversations with call center technicians."
                    Expanded Prompt: "Generate a detailed customer conversation with a call center technician. The conversation should present a unique scenario involving a customer issue and possible resolution. Pick a unique problem. Also pick a tone and level of complexity."

                    '''
    prefix = f'''Here is the prompt for to expand: 
    
                Input Prompt: {user_input}
            '''
    
    return system_prompt + prefix



def generate_actor_prompt(expanded_prompt: str) -> str:
    """
    Generates a prompt for the actor LLM.
    Adds a 'system prompt' for the actor LLM and cleans up the expanded prompt if necessary.
    
    Args:
        expanded_prompt (str): The expanded prompt.

    Returns:
        str: The actor prompt.
    """

    system_prompt = '''
                    You are a language model specialized in generating synthetic text data based on detailed, 
                    contextually rich instructions. Your goal is to create high-quality synthetic data that 
                    can be used for fine-tuning tasks. Ensure that the generated text is high-quality, while
                    also not being too generic.
                    '''
    # Clean up the expanded prompt?
    return system_prompt + expanded_prompt
