from abc import ABC, abstractmethod
from datetime import datetime

class Summary(ABC):
    def __init__(self, data):
        self.df = data

    def get_statistics(self, months_back: int):
        summaries = []
        for offset in range(months_back):
            month, year = self._get_month_by_offset(offset)
            summary = self._get_month_summary(month, year)
            summaries.append(summary)
        return summaries

    def _get_month_by_offset(self, offset: int):
        month = datetime.now().month - offset
        year = datetime.now().year
        if month <= 0:
            month += 12
            year -= 1
        return month, year
    
    @abstractmethod
    def _get_month_summary(self, month: int, year: int):
        pass