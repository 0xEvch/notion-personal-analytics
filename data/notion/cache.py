import pickle
import os

class Cache:
    def __init__(self, database_path: str, sync_cache_path: str):
        self.DB_CACHE = database_path
        self.SYNC_CACHE = sync_cache_path

    def is_synced(self, actual_id: str):
        last_id = self._load_sync_info()
        if actual_id == last_id:
            return True
        return False

    def save_sync_info(self, data):
        os.makedirs(os.path.dirname(self.SYNC_CACHE), exist_ok=True)
        try:
            with open(self.SYNC_CACHE, "wb") as f:
                pickle.dump(data, f)
        except pickle.PickleError as e:
            print(f"Caching error: {e}")
    
    def load_cache(self):
        if os.path.exists(self.DB_CACHE):
            try:
                with open(self.DB_CACHE, "rb") as f:
                    return pickle.load(f)
            except (pickle.PickleError, EOFError, ValueError) as e:
                print(f"Loading error: {e}")
                return None
        return None
    
    def save_cache(self, data):
        os.makedirs(os.path.dirname(self.DB_CACHE), exist_ok=True)
        try:
            with open(self.DB_CACHE, "wb") as f:
                pickle.dump(data, f)
        except pickle.PickleError as e:
            print(f"Caching error: {e}")
    
    def _load_sync_info(self)-> str:
        if os.path.exists(self.SYNC_CACHE):
            try:
                with open(self.SYNC_CACHE, "rb") as f:
                    return pickle.load(f)
            except (pickle.PickleError, EOFError, ValueError) as e:
                print(f"Loading error: {e}")
                return None
        return None

