from data.notion.notion_loader import NotionLoader
from core.utils.autopilot_json_parser import AutopilotJsonParser
from data.notion.cache import Cache
from data.notion.sync_manager import SyncManager
from core.utils.pandas_parser import PandasParser
from core.services.activity_summary import ActivitySummary
from core.views.charts_view import Histogram
from core.views.table_view import Tables
from backend.config import *

class Orchestrator:
    def run_analytics(self, months_back):
        loader = NotionLoader(TOKEN, AUTOPILOT)
        json_parser = AutopilotJsonParser()
        cache = Cache(AUTOPILOT_CACHE, AUTOPILOT_SYNC_CACHE)
        sync = SyncManager(loader, json_parser, cache)
        data = sync.get_data()

        pandas_parser = PandasParser()
        dataframe = pandas_parser.get_dataframe(data)
        summary = ActivitySummary(dataframe)
        analytics = summary.get_statistics(months_back)

        # histogram = Histogram()
        # histogram.create_chart(analytics)

        table = Tables()
        table.create_hours_table(analytics)

if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run_analytics(3)