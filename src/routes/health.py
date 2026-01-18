from fastapi import APIRouter
from src.controller import health


router = APIRouter()

router.get("/health", tags=["Health"])(health.health)
