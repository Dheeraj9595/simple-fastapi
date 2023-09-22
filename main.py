from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Welcome to fastapi project."}


@app.get("/hello")
def read_root():
    return {"message": "Hello, world!"}
