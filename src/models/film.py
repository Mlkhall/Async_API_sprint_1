import orjson
from datetime import date, datetime
from pydantic import confloat
from typing import Union
from uuid import UUID

# Используем pydantic для упрощения работы при перегонке данных из json в объекты
from pydantic import BaseModel


def orjson_dumps(v, *, default):
    # orjson.dumps возвращает bytes, а pydantic требует unicode, поэтому декодируем
    return orjson.dumps(v, default=default).decode()


class Config:
    # Заменяем стандартную работу с json на более быструю
    json_loads = orjson.loads
    json_dumps = orjson_dumps


class Film(BaseModel, Config):
    id: UUID
    title: str
    description: Union[str, None]
    creation_date: Union[date, None]
    certificate: Union[str, None]
    file_path: Union[str, None]
    rating: Union[confloat(ge=0, le=10), None]
    type: str
    created_at: datetime
    updated_at: datetime


class Genre(BaseModel, Config):
    id: UUID
    name: str
    description: Union[str, None]
    created_at: datetime
    updated_at: datetime


class GenreFilmWork(BaseModel, Config):
    id: UUID
    film_work_id: str
    genre_id: str
    created_at: datetime


class Person(BaseModel, Config):
    id: UUID
    full_name: str
    birth_date: date
    created_at: datetime
    updated_at: datetime


class PersonFilmWork(BaseModel, Config):
    id: UUID
    film_work_id: UUID
    person_id: UUID
    role: str
    created_at: datetime

