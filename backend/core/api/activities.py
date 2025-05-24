from fastapi import APIRouter
from .endpoints import autopilot

router = APIRouter(
    prefix="/activities",
    tags=["activities"]
)

@router.get("/")
async def get_time_bar_chart(months_back: int):
    pass