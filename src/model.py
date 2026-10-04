from enum import Enum

class Model:
    def __init__(
            self,
            model_name: str,
            context_length: int = 4096,
            temperature : float = 0.8
            ) -> None:
        self.model_name = model_name
        self.context_length = context_length
        self.temperature = temperature