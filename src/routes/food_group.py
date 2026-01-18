from typing import List
from fastapi import APIRouter
from src.controller import food_group as controller
from src.schemas.food_group import FoodGroupRead


router = APIRouter()

router.post("/food-group", tags=["Food Group"], response_model=FoodGroupRead)(controller.create_food_group)

router.get("/food-groups", tags=["Food Group"], response_model=List[FoodGroupRead])(controller.get_all_food_groups)

router.get("/food-group", tags=["Food Group"], response_model=FoodGroupRead)(controller.get_food_group_by_id)

router.put("/food-group", tags=["Food Group"], response_model=FoodGroupRead)(controller.update_food_group)

router.delete("/food-group", tags=["Food Group"])(controller.delete_food_group)
