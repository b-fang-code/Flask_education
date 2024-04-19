# Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов
# по заданному жанру.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Movie с полями id, title, description и genre.
# ● Создайте список movies для хранения фильмов.
# ● Создайте маршрут для получения списка фильмов по жанру (метод GET).
# ● Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Optional[str] = None


movies = []


@app.get('/{genre}')
async def get_movies_by_genre(genre: str):
    global movies
    logger.info('Get movies by genre')
    return {"movies": [movie for movie in movies if movie.genre == genre]}


@app.post('/')
async def create_movie(movie: Movie):
    global movies
    logger.info('Create movie')
    movies.append(movie)
    return {"movie": movie}


@app.put('/{movie_id}')
async def update_movie(movie_id: int, movie: Movie):
    global movies
    logger.info('Update movie')
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movies[i] = movie
            return {"movie": movie}
    return {"error": "Movie not found"}


@app.delete('/{movie_id}')
async def delete_movie(movie_id: int):
    global movies
    logger.info('Delete movie')
    for i in range(len(movies)):
        if movies[i].id == movie_id:
            movies.pop(i)
            return {"message": "Movie deleted"}
    return {"error": "Movie not found"}
