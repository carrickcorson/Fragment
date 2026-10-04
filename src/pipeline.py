import json
from pydantic import BaseModel

class Message:
    def __init__(
        self,
        model: str,
        message: str,
        message_format: object | None = None,
        options: object | None = None,
        think: bool | None = None,
        keep_alive: str | None = None) -> None:

        self.model = model
        self.message_format = message_format
        self.options = options
        self.think = think
        self.keep_alive = keep_alive

        self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, obj: object):
        m = json.loads(obj)

        if not m["user"]:
            raise IndexError("Message requires 'user' field")

        if not m["assistant"]:
            raise IndexError("Message requires 'assistant' field")      

        self._message = obj


    def formatted(self) -> object:
        return json.dumps({"model": self.model,
                "message": self.message,
                "format": self.message_format,
                "options": self.options,
                "think": self.think,
                "keep_alive": self.keep_alive})

class Response(BaseModel):
    model: str
    created_at: str
    message: object
    done: bool
    done_reason: str
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_cache_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int
    logprobs: object