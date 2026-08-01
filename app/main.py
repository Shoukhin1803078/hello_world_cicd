from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello world!. This is My First CICD for learning"}