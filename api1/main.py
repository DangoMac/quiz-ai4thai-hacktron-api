from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api1")
def call_api2():
    print("API1: Received request from user")
    try:
        #ของ docker
        #response = requests.get("http://api2:8001/api2")
        #ของ local
        response = requests.get("http://127.0.0.1:8001/api2")
        print("API1: Forwarded request to API2")
        return {"message": f"API1: Got response from API2: {response.text}"}
    except Exception as e:
        return {"error": str(e)}
