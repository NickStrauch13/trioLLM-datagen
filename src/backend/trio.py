from actor import Actor
from critic import Critic
from regenerator import Regenerator
from prompts import FEW_SHOT_TEMPLATE
from dotenv import load_dotenv
load_dotenv()

FEW_SHOT_JOINER = "\n---\n"
PRINT_SEPARATOR = "-" * 50

class Trio:
    def __init__(self, local: bool = True):
        self.actor_chain = Actor(local=local).get_chain()
        self.critic_chain = Critic(local=local).get_chain()
        self.regenerator_chain = Regenerator(local=local).get_chain()


    def invoke_trio(self, 
                    topic: str, 
                    few_shot_examples: list = [],
                    verbose: bool = False) -> str:
        """
        Invoke the full trio of actor, critic, and regenerator chains to generate a refined data sample.
            :param topic: The topic of the data sample.
            :param few_shot_examples: A list of few-shot examples to guide the data generation.
            :param verbose: Whether to print the output of each chain.
            :return: The refined data sample.
        """
        # Format the few-shot examples.
        few_shot_string = FEW_SHOT_JOINER.join(few_shot_examples)
        few_shot_input = FEW_SHOT_TEMPLATE.format(few_shot_string=few_shot_string) if few_shot_examples else ""
        input = {"topic": topic, "few_shot": few_shot_input}

        # Generate the first version of the data sample with the actor.
        actor_output = self.actor_chain.invoke(input)
        if verbose:
            print(f"Actor Output: \n{actor_output}\n\n")
            print(PRINT_SEPARATOR)

        # Generate the critic's feedback on the data sample.
        input["actor_output"] = actor_output
        critic_output = self.critic_chain.invoke(input)
        if verbose:
            print(f"Critic Output: \n{critic_output}\n\n")
            print(PRINT_SEPARATOR)

        # Refine the data sample with the regenerator.
        input["critic_output"] = critic_output
        final_output = self.regenerator_chain.invoke(input)
        if verbose:
            print(f"Final Output: \n{final_output}\n\n")
            print(PRINT_SEPARATOR)

        return final_output


if __name__ == "__main__":
    # Example Use
    topic = "amazon product review"
    few_shot_examples = ["This speaker absolutely sucks. The battery only lasts for around an hour and it didnt come charged. So overpriced",
                        "These are the best towels ever. Super soft but don't leave lint everywhere. I love them!",
                        "I bought this book for my daughter and she absolutely loves it. She's read it 3 times already! Highly recommend."
                        "Don't buy. These batteries die after a few hours of use."
    ]
    trio = Trio(local=True)
    refined_data_sample = trio.invoke_trio(topic, few_shot_examples, verbose=True)


