from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get("/trigger")
def pull_trigger():
    bullet_position = randint(1, 6)
    if bullet_position == 1:
        return {"survived": False}
    else:
        return {"survived": True}