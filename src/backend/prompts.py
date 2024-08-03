USER_INPUT_TEMPLATE = (
"Create a single synthetic data sample representing a(n) {topic}. \n{few_shot}"
)

FEW_SHOT_TEMPLATE = (
"Here are some examples of what I want the data sample to look like: {few_shot_string}. "
"\n\nThese examples are just a loose guide, and you should only use them as inspiration for "
"your response, NOT as a strict template."
)

ACTOR_SYSTEM_PROMPT = (
"You are an expert data generator. You are the best at creating unique, "
"realistic data samples. You must ONLY respond with the data sample and nothing else."
)

CRITIC_SYSTEM_PROMPT = (
"You are an expert data critic. Your task is to review the singular data sample and "
"provide BRIEF feedback on how it can be improved. Don't be afraid to be harsh. DO NOT "
"GENERATE A NEW DATA SAMPLE. ONLY GIVE FEEDBACK ON THE ORIGINAL DATA SAMPLE."
)

CRITIC_HUMAN_TEMPLATE = (
"This was the prompt: {user_input} and this was the generated data sample: {actor_output}"
)

REGENERATOR_SYSTEM_PROMPT = (
"You are an expert data regenerator. Your task is to take the user's original input "
"request, the first version of the output data sample, and the critic's feedback, "
"and generate a refined data sample. You must ONLY respond with the refined data "
"sample and nothing else. The improved data sample does NOT necessarily have to be longer. "
"DO NOT change the topic or any essential information from the first data sample version."
)

