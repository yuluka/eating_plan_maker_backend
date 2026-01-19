from typing import List
from fastapi import APIRouter
from src.controller import micronutrient_group as controller
from src.schemas.micronutrient_group import MicronutrientGroupRead


router = APIRouter()

router.post("/micronutrient-group", tags=["Micronutrient Group"], response_model=MicronutrientGroupRead)(controller.create_micronutrient_group)

router.get("/micronutrient-groups", tags=["Micronutrient Group"], response_model=List[MicronutrientGroupRead])(controller.get_all_micronutrient_groups)

router.get("/micronutrient-group", tags=["Micronutrient Group"], response_model=MicronutrientGroupRead)(controller.get_micronutrient_group_by_id)

router.put("/micronutrient-group", tags=["Micronutrient Group"], response_model=MicronutrientGroupRead)(controller.update_micronutrient_group)

router.delete("/micronutrient-group", tags=["Micronutrient Group"])(controller.delete_micronutrient_group)
