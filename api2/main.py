from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/api2")
def pull_trigger():
    print("API2: Received request from API1")
    bullet_position = randint(1, 6)
    if bullet_position == 1:
        return {"survived": False}
    else:
        return {"survived": True}