from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config import settings
from src.routes.health import router as health_router
from src.routes.food_group import router as food_group_router
from src.routes.food_moment import router as food_moment_router
from src.routes.macronutrient_group import router as macronutrient_group_router

app = FastAPI(
    root_path=settings.CONTEXT_PATH,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(health_router)
app.include_router(food_group_router)
app.include_router(food_moment_router)
app.include_router(macronutrient_group_router)
