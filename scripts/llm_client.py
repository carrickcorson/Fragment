import requests
import json
from enum import StrEnum
from collections.abc import Generator

class Model(StrEnum):
    GENERAL = "phi3"
    REASONING = "mistral"
    CODING = "deepseek-coder:6.7b"

class LocalLLM:
    def __init__(
            self,
            model: Model,
            url: str = "http://localhost:11434/v1/chat/completions",
            max_tokens: int = 400,
            temperature: float = 0.2
        ) -> None:

        self.url = url
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def chat(
            self,
            messages: list,
        ) -> Generator[str, None, None]:

        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "stream": True
        }

        response = requests.post(self.url, json=payload, stream=True)
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data: "):
                    raw_line = decoded_line[6:]
                
                if raw_line == "[DONE]":
                    break

                data = json.loads(raw_line)
                delta = data['choices'][0]['delta'].get('content', '')
                
                if delta:
                    yield delta
        
        response.raise_for_status()
