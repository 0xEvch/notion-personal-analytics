from abc import ABC, abstractmethod
from datetime import datetime
from data.notion.sync_manager import SyncManager
from core.utils.pandas_parser import PandasParser

class Summary(ABC):
    def __init__(self):
        data = SyncManager.get_autopilot_data()
        self.df = PandasParser.get_autopilot_dataframe(data)


    def get_statistics(self, months_back):
        summaries = []
        for offset in range(1, months_back + 1):
            month, year = self._get_month_by_offset(offset)
            summary = self._get_month_summary(month, year)
            summaries.append(summary)
        return summaries

    def _get_month_by_offset(self, offset):
        month = datetime.now().month - offset
        year = datetime.now().year
        if month <= 0:
            month += 12
            year -= 1
        return month, year
    
    @abstractmethod
    def _get_month_summary(self, month: int, year: int):
        pass