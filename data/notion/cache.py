import pickle
import os
from typing import List
from core.models.autopilot import Autopilot

AUTOPILOT_CACHE = "data/cache/autopilot_cache.pkl"
SYNC_CACHE = "data/cache/sync_config.pkl"

class Cache:
    @staticmethod
    def is_synced(actual_id):
        last_id = Cache._load_sync_info()
        if actual_id == last_id:
            return True
        return False

    @staticmethod
    def save_sync_info(data):
        os.makedirs(os.path.dirname(SYNC_CACHE), exist_ok=True)
        try:
            with open(SYNC_CACHE, "wb") as f:
                pickle.dump(data, f)
        except pickle.PickleError as e:
            print(f"Caching error: {e}")
    
    @staticmethod
    def load_cache() -> List[Autopilot]:
        if os.path.exists(AUTOPILOT_CACHE):
            try:
                with open(AUTOPILOT_CACHE, "rb") as f:
                    return pickle.load(f)
            except (pickle.PickleError, EOFError, ValueError) as e:
                print(f"Loading error: {e}")
                return None
        return None

    @staticmethod
    def save_cache(data: List[Autopilot]):
        os.makedirs(os.path.dirname(AUTOPILOT_CACHE), exist_ok=True)
        try:
            with open(AUTOPILOT_CACHE, "wb") as f:
                pickle.dump(data, f)
        except pickle.PickleError as e:
            print(f"Caching error: {e}")
    
    @staticmethod
    def _load_sync_info()-> str:
        if os.path.exists(SYNC_CACHE):
            try:
                with open(SYNC_CACHE, "rb") as f:
                    return pickle.load(f)
            except (pickle.PickleError, EOFError, ValueError) as e:
                print(f"Loading error: {e}")
                return None
        return None

