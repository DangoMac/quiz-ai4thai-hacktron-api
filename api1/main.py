from fastapi import FastAPI, Query
import requests
from datetime import datetime

app = FastAPI()

@app.get("/russian-roulette")
def play(player: str = Query(...)):
    try:
        res = requests.get("http://127.0.0.1:8001/trigger")
        survived = res.json().get("survived")
        if survived:
            result = "Click! You survived."
        else:
            result = "Bang! You died!"
            
        return {
            "player": player,
            "result": result,
        }
    
    except Exception as e:
        return {"error": "Could not complete the game"}