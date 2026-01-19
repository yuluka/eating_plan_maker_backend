from typing import List
from fastapi import APIRouter
from src.controller import special_condition as controller
from src.schemas.special_condition import SpecialConditionRead


router = APIRouter()

router.post("/special-condition", tags=["Special Condition"], response_model=SpecialConditionRead)(controller.create_special_condition)

router.get("/special-conditions", tags=["Special Condition"], response_model=List[SpecialConditionRead])(controller.get_all_special_conditions)

router.get("/special-condition", tags=["Special Condition"], response_model=SpecialConditionRead)(controller.get_special_condition_by_id)

router.put("/special-condition", tags=["Special Condition"], response_model=SpecialConditionRead)(controller.update_special_condition)

router.delete("/special-condition", tags=["Special Condition"])(controller.delete_special_condition)
