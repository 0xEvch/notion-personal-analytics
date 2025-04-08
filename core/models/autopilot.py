from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Autopilot:
    name: str
    activity_type: str
    date: datetime
    duration_min: int
    duration_hrs: float
    notes: Optional[str] = None
    
