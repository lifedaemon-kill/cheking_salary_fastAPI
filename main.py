from fastapi import FastAPI

app = FastAPI(
    title = "test FastAPI"
    )

@app.get("/")
def hello():
    return "hello world!"
