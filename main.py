from fastapi import FastAPI

app = FastAPI()

@app.get("/sample")
def read_root():
    print("call API!")
    return {"message": "First FastAPI!!"}
