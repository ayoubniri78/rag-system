from fastapi import APIRouter

from .data import data_router


router = APIRouter()

router.include_router(data_router)
