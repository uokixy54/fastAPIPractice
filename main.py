from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("call API!")
    return {"message": "First FastAPI!!"}
