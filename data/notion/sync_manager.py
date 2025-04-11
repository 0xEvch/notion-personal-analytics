from typing import List
from core.models.autopilot import Autopilot
from data.notion.notion_loader import NotionLoader
from data.notion.cache import Cache
from config import token

class SyncManager:
    _cached_autopilot_objects = []

    @staticmethod
    def get_autopilot_data() -> List[Autopilot]:
        global _cached_autopilot_objects

        loader = NotionLoader(token)
        actual_id = loader.sync_query()
        
        if Cache.is_synced(actual_id):
            print("load from file")
            _cached_autopilot_objects = Cache.load_cache()
        else:
            print("load from API")
            _cached_autopilot_objects = loader.get_database()
            Cache.save_cache(_cached_autopilot_objects)
            Cache.save_sync_info(actual_id)

        return _cached_autopilot_objects
    
if __name__ == "__main__":
    SyncManager.get_autopilot_data()