from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",                            # React Appのテスト用URL
    "https://uokixy54.github.io/ProjectStaticQuiz-/",   # GitHub PagesのURL
    "https://testpythonapi.herokuapp.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sample")
async def read_root():
    return {"message": "First FastAPI!!"}
