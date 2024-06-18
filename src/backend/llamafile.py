from openai import OpenAI


client = OpenAI(
    base_url= "http://127.0.0.1:8080/v1",
    api_key="sk-none"
)

completion = client.chat.completions.create(
    model="LLaMA_CPP",
    messages=[
        {"role": "system", "content": "You are a great language model. You answer questions and generate text based on the user's input."},
        {"role": "user", "content": "Write a funny joke about nature."}
    ],
    temperature=0.5
)

print(completion.choices[0].message)