import requests
from rich import print

from .base_translator import Base


class GPT3(Base):
    def __init__(self, key, language, api_base=None):
        super().__init__(key, language)
        self.api_key = key
        self.api_url = (
            f"{api_base}v1/completions"
            if api_base
            else "https://api.openai.com/v1/completions"
        )
        self.headers = {
            "Content-Type": "application/json",
        }
        # TODO support more models here
        self.data = {
            "prompt": "",
            "model": "text-davinci-003",
            "max_tokens": 1024,
            "temperature": 1,
            "top_p": 1,
        }
        self.session = requests.session()
        self.language = language

    def translate(self, text):
        print(text)
        self.headers["Authorization"] = f"Bearer {self.get_key(self.api_key)}"
        self.data[
            "prompt"
        ] = f"I want you to act as an {self.language} translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in {self.language}. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level {self.language} words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations, the text is: \n\n{text}"
        r = self.session.post(self.api_url, headers=self.headers, json=self.data)
        if not r.ok:
            return text
        t_text = r.json().get("choices")[0].get("text", "").strip()
        print(t_text)
        return t_text
