from openai import OpenAI

file=open("aimlapi_key.txt","r")
key=file.read()

base_url = "https://api.aimlapi.com/v1"
api_key = key
system_prompt = "You are a cyber case classifier consultant. Be descriptive and helpful."
user_prompt = "Tell me what the penalties and jail time are for an offense of possession or use of tools or software intended for cybercrime and public interest litigation."

api = OpenAI(api_key=api_key, base_url=base_url)

completion = api.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ],
    temperature=0.7,
    max_tokens=25,
)

response = completion.choices[0].message.content

print("User:", user_prompt)
print("AI:", response)

