from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Autopilot:
    name: str
    activity_type: str
    date: date
    duration_min: int
    duration_hrs: float
    notes: Optional[str] = None