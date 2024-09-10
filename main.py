from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://uokixy54.github.io/ProjectStaticQuiz-/"  # GitHub PagesのURL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sample")
def read_root():
    print("call API!")
    return {"message": "First FastAPI!!"}
