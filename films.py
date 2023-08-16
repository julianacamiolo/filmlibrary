from fastapi import APIRouter, Path
from typing import List, Dict

router = APIRouter()

films_data = [
    {
        "id": 1,
        "name": "Film 1",
        "price": 5,
        "stock": 40
    },
    {
        "id": 2,
        "name": "Film 2",
        "price": 10,
        "stock": 30
    },
    {
        "id": 3,
        "name": "Film 3",
        "price": 8,
        "stock": 20
    }
]

@router.get('/')
def message():
    return "I love films"

@router.get('/films')
def get_films():
    return films_data

@router.get('/films/{film_id}')
def get_film_by_id(film_id: int = Path(..., title="Film ID")):
    return next((film for film in films_data if film["id"] == film_id), None)

@router.get('/films/by_stock')
def get_films_by_stock(stock: int):
    return [film for film in films_data if film["stock"] == stock]

@router.get('/films/by_price')
def get_films_by_price(price: int):
    return [film for film in films_data if film["price"] == price]

@router.post('/films')
def create_film(new_film: Dict):
    films_data.append(new_film)
    return new_film

@router.put('/films/{film_id}')
def update_film(film_id: int, updated_film: Dict):
    for film in films_data:
        if film["id"] == film_id:
            film.update(updated_film)
            return film
    return {"message": "Film not found"}

@router.delete('/films/{film_id}')
def delete_film(film_id: int):
    for film in films_data:
        if film["id"] == film_id:
            films_data.remove(film)
            return {"message": "Film deleted"}
    return {"message": "Film not found"}