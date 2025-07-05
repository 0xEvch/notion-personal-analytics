from data.notion_loader import NotionLoader
from core.utils.base_json_parser import JsonParser
from data.cache import Cache

class SyncManager:
    def __init__(self, loader: NotionLoader, parser: JsonParser, cache: Cache):
        self.loader = loader
        self.parser = parser
        self.cache = cache

    def get_data(self):
        actual_id = self.loader.sync_query()
        
        if self.cache.is_synced(actual_id):
            return self.cache.load_cache()
        else:
            raw_data = self.loader.get_database()
            data = self.parser.parse_notion_data(raw_data)
            self.cache.save_cache(data)
            self.cache.save_sync_info(actual_id)
            print(data)
            return data