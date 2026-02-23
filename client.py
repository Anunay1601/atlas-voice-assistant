from openai import OpenAI
# client = OpenAI()

client = OpenAI(
    api_key="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" ,
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
        {
            "role": "user",
            "content": "what is coding."
        }
    ]
)

print(completion.choices[0].message.content)
