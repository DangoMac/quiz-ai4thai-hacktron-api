from fastapi import FastAPI, Query
import requests
from datetime import datetime

app = FastAPI()

@app.get("/api1")
def play(player: str = Query(...)):
    try:
        #ของ local
        #res = requests.get("http://127.0.0.1:8001/api2")
        print("API1: Forwarded request to API2")
        res = requests.get("http://api2:8001/api2")
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