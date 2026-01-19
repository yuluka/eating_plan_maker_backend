from typing import List
from fastapi import APIRouter
from src.controller import macronutrient_group as controller
from src.schemas.macronutrient_group import MacronutrientGroupRead


router = APIRouter()

router.post("/macronutrient-group", tags=["Macronutrient Group"], response_model=MacronutrientGroupRead)(controller.create_macronutrient_group)

router.get("/macronutrient-groups", tags=["Macronutrient Group"], response_model=List[MacronutrientGroupRead])(controller.get_all_macronutrient_groups)

router.get("/macronutrient-group", tags=["Macronutrient Group"], response_model=MacronutrientGroupRead)(controller.get_macronutrient_group_by_id)

router.put("/macronutrient-group", tags=["Macronutrient Group"], response_model=MacronutrientGroupRead)(controller.update_macronutrient_group)

router.delete("/macronutrient-group", tags=["Macronutrient Group"])(controller.delete_macronutrient_group)
