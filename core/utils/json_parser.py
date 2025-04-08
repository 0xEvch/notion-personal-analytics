from core.models.autopilot import Autopilot
from datetime import date
from typing import List

class JsonParser:
    @staticmethod
    def parse_notion_data(data) -> List[Autopilot]:
        autopilot_objects = []

        properties = data.get("results", [])
        for item in properties:
            autopilot = Autopilot(
                name = JsonParser._parse_title(item),
                activity_type = JsonParser._parse_activity_type(item),
                date = JsonParser._parse_date(item), 
                duration_min = JsonParser._parse_duration_min(item),
                duration_hrs = JsonParser._parse_duration_hrs(item),
                notes = JsonParser._parse_notes(item),
            )
            autopilot_objects.append(autopilot)

    @staticmethod
    def _parse_title(properties) -> str:
        return properties["properties"]["Name"]["title"][0]["text"]["content"]
    
    @staticmethod
    def _parse_activity_type(properties) -> str:
        return properties["properties"]["Activity type"]["select"]["name"]
    
    @staticmethod
    def _parse_date(properties) -> date:
        date_str = properties["properties"]["Date"]["date"]["start"]
        return date.fromisoformat(date_str)
    
    @staticmethod
    def _parse_duration_min(properties) -> int:
        return properties["properties"]["Time (min)"]["number"]
    
    @staticmethod
    def _parse_duration_hrs(properties) -> str:
        return properties["properties"]["Hrs"]["formula"]["number"]
    
    @staticmethod
    def _parse_notes(properties) -> str:
        try:
            rich_text = properties["properties"]["Notes"]["rich_text"]
            if rich_text:
                return rich_text["plain_text"]
        except:
            return None