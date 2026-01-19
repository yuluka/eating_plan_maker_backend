from typing import List
from fastapi import APIRouter
from src.controller import food_moment as controller
from src.schemas.food_moment import FoodMomentRead


router = APIRouter()

router.post("/food-moment", tags=["Food Moment"], response_model=FoodMomentRead)(controller.create_food_moment)

router.get("/food-moments", tags=["Food Moment"], response_model=List[FoodMomentRead])(controller.get_all_food_moments)

router.get("/food-moment", tags=["Food Moment"], response_model=FoodMomentRead)(controller.get_food_moment_by_id)

router.put("/food-moment", tags=["Food Moment"], response_model=FoodMomentRead)(controller.update_food_moment)

router.delete("/food-moment", tags=["Food Moment"])(controller.delete_food_moment)
