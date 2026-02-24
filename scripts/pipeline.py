import time
from collections.abc import Generator
from llm_client import LocalLLM, Model
from dataclasses import dataclass


class DebugMessage:
    def __init__(
            self,
            text: str
        ) -> None:

        print(f"{time.strftime("%H:%M:%S", time.localtime())} [DEBUG] {text}")


@dataclass
class Keywords:
    
    reasoning = ("why",
                 "explain",
                 "tell me")
    
    coding = ("script",
              "code",
              "function",
              "class")

class Pipeline:
    def __init__(
            self,
            url: str = "http://localhost:11434/v1/chat/completions"
        ) -> None:

        self.model_general = LocalLLM(
            Model.GENERAL,
            url=url,
            max_tokens=400,
            temperature=0.5
        )

        self.model_reasoning = LocalLLM(
            Model.REASONING,
            url=url,
            max_tokens=400,
            temperature=0.3
        )

        self.model_coding = LocalLLM(
            Model.CODING,
            url=url,
            max_tokens=400,
            temperature=0.2
        )


    def _determine_model(
            self,
            recent_prompt: str
        ) -> LocalLLM:

        if any(word in recent_prompt for word in Keywords.reasoning):
            model = self.model_reasoning

        elif any(word in recent_prompt for word in Keywords.coding):
            model = self.model_coding
        
        else:
            model = self.model_general
        
        return model
    
    def chat(
        self,
        messages: list
        ) -> Generator[str, None, None]:

        recent_user_prompt = messages[-1]["content"]

        model = self._determine_model(recent_user_prompt)
        
        yield from model.chat(messages)



