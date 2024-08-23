from openai import OpenAI
client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write first paragraph of twinkle twinkle little star poem"
        }
    ]
)

print(completion.choices[0].message)