from models.autopilot import Autopilot
import json

class JsonParser:
    def parse_notion_data(data: str) -> Autopilot:
        json_data = json.loads(data)
        
        autopilot_objects = []

        properties = json_data.get("results", [])
        for item in properties.get("properties", []):
            print(item.get("name", {}).get("title", [{}])[0].get("text", {}).get("content", ""))