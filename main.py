import uvicorn
from fastapi import FastAPI, HTTPException


app = FastAPI()


movies = [
    {
        "id": 1,
        "title": "Naked gun"
    },
    {
        "id": 2,
        "title": "Friends"
    },
]

@app.get("/movie", tags=["Movie"])
def my_movie():
    return movies

@app.get("/movie/{id}", tags=["Movie"])
def get_movie(movie_id: int):
    for m in movies:
        if m["id"] == movie_id:
            return m
    raise HTTPException(status_code=404, detail="Movie doesn't found")

# @app.get('/', summary="Главная функция", tags=["Основная функция"])
# def home():
#     return "Hello world!!!"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
