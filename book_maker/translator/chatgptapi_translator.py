import time

import openai

from .base_translator import Base


class ChatGPTAPI(Base):
    def __init__(self, key, language, api_base=None):
        super().__init__(key, language, api_base=api_base)
        self.key = key
        self.language = language
        if api_base:
            openai.api_base = api_base

    def translate(self, text):
        print(text)
        openai.api_key = self.get_key(self.key)
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        # english prompt here to save tokens
                        "content": f"I want you to act as an {self.language} translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in {self.language}. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level {self.language} words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations, the text is: \n\n{text}",
                    }
                ],
            )
            t_text = (
                completion["choices"][0]
                .get("message")
                .get("content")
                .encode("utf8")
                .decode()
            )
        except Exception as e:
            # TIME LIMIT for open api please pay
            key_len = self.key.count(",") + 1
            sleep_time = int(60 / key_len)
            time.sleep(sleep_time)
            print(e, f"will sleep  {sleep_time} seconds")
            openai.api_key = self.get_key(self.key)
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": f"I want you to act as an {self.language} translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in {self.language}. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level {self.language} words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations, the text is: \n\n{text}",
                    }
                ],
            )
            t_text = (
                completion["choices"][0]
                .get("message")
                .get("content")
                .encode("utf8")
                .decode()
            )
        print(t_text)
        return t_text
