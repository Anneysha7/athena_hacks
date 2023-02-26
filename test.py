import openai

openai.api_key = "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"
prompt = "Say hello world"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)
print(response)