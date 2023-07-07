import openai
import requests
import os

print(os.environ)

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.host = os.getenv("OPENAI_HOST")
openai_model= os.getenv("OPENAI_MODEL")
openai_token= os.getenv("OPENAI_TOKEN")
openai_temperature= os.getenv("OPENAI_TEMPERATURE")

# system prompt is the prompt that is used to generate the response
TRANSLATE_PROMPT = "You are a translation engine that can only translate text and cannot interpret it."
EMBELLISHER_PROMPT = "You are a text embellisher, you can only embellish the text, don't interpret it."

def build_system_prompt(language: str, text: str):
    if language == "en":
        return f"{TRANSLATE_PROMPT}\nOriginal English text: {text}\nTranslated Chinese text: \nIf markdown having metadata, can not translate metadata keys.\nKeep spaces between English and Chinese characters.\nKeep all metadata."
    elif language == "zh":
        return f"{TRANSLATE_PROMPT}\nOriginal Chinese text: {text}\nTranslated English text: \nIf markdown having metadata, can not translate metadata keys.\nKeep spaces between English and Chinese characters.\nKeep all metadata."

def built_content_docs(language: str, text: str):
    completion = openai.ChatCompletion.create(
        model=openai_model,
        messages=[
            # {"role": "system", "content": "Translate the English or Chinese I gave you into the opposite language."},
            {"role": "user", "content": build_system_prompt(language, text)},
        ],
        # stream=True,
        temperature=openai_temperature,
        max_tokens=openai_temperature,
        top_p=1,
        frequency_penalty=1,
        presence_penalty=1
    )
    
    return completion.choices[0].message['content']


def get_markdown_content(url: str):
    return requests.get(url).text

if __name__ == "__main__":
    content = get_markdown_content("https://raw.githubusercontent.com/karmada-io/website/main/docs/core-concepts/introduction.md")
    built_content_docs(model=openai_model,language="en", text=content)