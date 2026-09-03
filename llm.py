from groq import Groq

llm_client = Groq(api_key="")

user_prompt = input('Enter The Prompt : ')

llm_model = llm_client.chat.completions.create(
    model="openai/gpt-oss-120b",
    temperature=0.25,
    messages=[
        {
            "role" : 'system',
            "content" : "Act as a AIML Trainer and give me most grounded response"
        },
        {
            "role" : 'system',
            "content" : user_prompt
        }
    ]
)

llm_response = llm_model.choices[0].message.content
print(llm_response)