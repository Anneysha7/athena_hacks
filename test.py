import openai

openai.api_key = "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"

poem_language = ""
translation_language = ""
type = ""
theme = ""

prompt = f"{poem_language} {type} based on {theme} with a translation in {translation_language}"

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=6)
print(response)