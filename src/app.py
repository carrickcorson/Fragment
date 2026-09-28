from fastapi import FastAPI

fragment_app = FastAPI()

@fragment_app.get("/")
async def main():
    return {"message": "Hellooooo"}