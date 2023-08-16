from fastapi import FastAPI, Query, Path
from models.films import films
from typing import List, Dict
from router.films import router as films_router

app = FastAPI()
app.include_router(films_router)

