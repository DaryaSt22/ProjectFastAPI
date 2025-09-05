import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/', summary="Главная функция", tags=["Основная функция"])
def home():
    return "Hello world!!!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
