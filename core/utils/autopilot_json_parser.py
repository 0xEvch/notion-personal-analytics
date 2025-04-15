from core.models.autopilot import Autopilot
from core.utils.base_json_parser import JsonParser
from datetime import date
from typing import List

class AutopilotJsonParser(JsonParser):
    def parse_notion_data(self, data) -> List[Autopilot]:
        autopilot_objects = []

        for item in data:
            autopilot = Autopilot(
                name = self._parse_title(item),
                activity_type = self._parse_activity_type(item),
                date = self._parse_date(item), 
                duration_min = self._parse_duration_min(item),
                duration_hrs = self._parse_duration_hrs(item),
                notes = self._parse_notes(item),
            )
            autopilot_objects.append(autopilot)
        return autopilot_objects

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
    def _parse_duration_hrs(properties) -> float:
        return properties["properties"]["Hrs"]["formula"]["number"]
    
    @staticmethod
    def _parse_notes(properties) -> str:
        try:
            return properties["properties"]["Notes"]["rich_text"][0]["plain_text"]
        except Exception as e:
            return None