from data.notion.notion_loader import NotionLoader
from core.utils.autopilot_json_parser import AutopilotJsonParser
from data.notion.cache import Cache
from data.notion.sync_manager import SyncManager
from core.utils.pandas_parser import PandasParser
from core.services.activity_summary import ActivitySummary
from core.views.activity_charts import ActivityChartView
from config import *
from fastapi import HTTPException

class Orchestrator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = curriculum = super().__new__(cls)
            cls._instance._init_data()
        return cls._instance

    def _init_data(self):
        self.loader = NotionLoader(TOKEN, AUTOPILOT)
        self.json_parser = AutopilotJsonParser()
        self.activity_cache = Cache(AUTOPILOT_CACHE, AUTOPILOT_SYNC_CACHE)
        self.sync = SyncManager(self.loader, self.json_parser, self.activity_cache)
        self.pandas_parser = PandasParser()
        self.activity_summary = ActivitySummary()
        self.activity_chart = ActivityChartView()

        try:
            raw_data = self.sync.get_data()
            self.activity_df = self.pandas_parser.get_dataframe(raw_data)
        except Exception as e:
            raise RuntimeError(f"Failed to initialize data: {e}")

    async def get_dataframe(self):
        if self.activity_df is None:
            raise HTTPException(status_code=500, detail="Data not initialized")
        return self.activity_df

    async def get_summary(self):
        return self.activity_summary

    async def get_chart(self):
        return self.activity_chart

if __name__ == "__main__":
    orchestrator = Orchestrator()