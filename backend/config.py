import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
AUTOPILOT = os.getenv("AUTOPILOT")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, 'data', 'cache')

AUTOPILOT_CACHE = os.path.join(CACHE_DIR, 'autopilot.json')
AUTOPILOT_SYNC_CACHE = os.path.join(CACHE_DIR, 'autopilot-sync.json')