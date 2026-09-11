from fastapi import FastAPI,APIRouter
from helpers.config import get_settings

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"]
)
