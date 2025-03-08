from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API"}

@app.get("/get")
def read_root():
    return {
        "name": "Felipe",
        "lastname": "Lopez",
        "age": 19,
        "id": 1234,
        "address": "Armenia/Quindio"
    }
