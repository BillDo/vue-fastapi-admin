from fastapi import APIRouter

from .base import router

base_router = APIRouter()
base_router.include_router(router, tags=["Basic Module"])

__all__ = ["base_router"]
