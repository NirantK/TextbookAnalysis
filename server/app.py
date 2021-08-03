import logging
from functools import lru_cache
from pathlib import Path
from typing import Optional, Union

from fastapi import FastAPI
from fastapi.logger import logger

logger.setLevel(logging.DEBUG)

PathLike = Union[Path, str]

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Textbook Analysis API"}