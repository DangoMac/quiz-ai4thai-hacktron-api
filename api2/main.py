from fastapi import FastAPI

app = FastAPI()

@app.get("/api2")
def say_hello():
    print("API2: Received request from API1")
    return {"message": "Hello from API2!"}
