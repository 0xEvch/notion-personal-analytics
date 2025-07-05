from data.notion_loader import NotionLoader
from core.utils.autopilot_json_parser import AutopilotJsonParser
from data.cache import Cache
from data.sync_manager import SyncManager
from core.utils.pandas_parser import PandasParser
from core.services.activity_summary import ActivitySummary
from core.views.charts_view import Histogram
from config import *

class AnalyzerCore():
    def __init__(self, table):   
        self._setup_mappings()

        if table not in self.data_providers:
            raise ValueError(f"Unknown data type: {table}")
        self.table = table
    
        self._initialize_components()

    def run_analytics(self, months_back):
        raw_data = self.sync_manager.get_data()
        data = self.pandas_parser.get_dataframe(raw_data)
        summary = self.analyzer.get_statistics_for_n_months_bar_chart(data, months_back)
        chart = self.view.get_chart(summary)

        print(summary)

    def _initialize_components(self):
        loader = self.data_providers[self.table]()
        json_parser = self.json_parsers[self.table]()
        cache = self.caches[self.table]()
        self.pandas_parser = PandasParser()
        self.sync_manager = SyncManager(loader, json_parser, cache)
        self.analyzer = self.analyzers[self.table]()
        self.view = self.views[self.table]()
    
    def _setup_mappings(self):
        self.data_providers = {
            "autopilot": lambda: NotionLoader(TOKEN, AUTOPILOT),
        }
        self.caches = {
            "autopilot": lambda: Cache(AUTOPILOT_CACHE, AUTOPILOT_SYNC_CACHE)
        }
        self.json_parsers = {
            "autopilot": lambda: AutopilotJsonParser(),
            # "new_table": NewTableParser(),
        }
        self.analyzers = {
            "autopilot": lambda: ActivitySummary(),
            # "new_table": NewTableSummary(),
        }
        self.views = {
            "autopilot": lambda: Histogram(),
        }

if __name__ == "__main__":
    test = AnalyzerCore("autopilot")
    test.run_analytics(3)