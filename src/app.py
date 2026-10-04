from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
from pipeline import Message, Response

FRAGMENT_URL = "https://192.168.1.200"
FRAGMENT_PORT = 8000

fragment_app = FastAPI()

@fragment_app.get("/")
async def main():
    return {"message": "Hellooooo"}

@fragment_app.post("/chat")
async def chat(message: Message) -> Response:
    return message


def send(message: Message):
    url = FRAGMENT_URL + ":" + str(FRAGMENT_PORT)
    payload = message
    response = requests.post(url, params=payload)
    return response.json()