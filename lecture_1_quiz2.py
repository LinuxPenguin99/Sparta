import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = ""

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "마라탕 레시피",
        }
    ],
    model="gpt-4o",
)

print(chat_completion.choices[0].message.content)
