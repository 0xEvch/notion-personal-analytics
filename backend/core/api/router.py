from fastapi import APIRouter
from .endpoints import autopilot

router = APIRouter()

router.include_router(
    autopilot.router,
    prefix="/api/autopilot",
    tags=["autopilot"]
)