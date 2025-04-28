from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd

class Summary(ABC):
    def get_statistics(self, data, months_back: int):
        summaries = []
        for offset in range(months_back):
            month, year = self._get_month_by_offset(offset)
            summary = self._get_month_summary(data, month, year)
            summary = self._add_month(summary, month)
            summaries.append(summary)
        return pd.concat(summaries, ignore_index=True)

    def _get_month_by_offset(self, offset: int):
        month = datetime.now().month - offset
        year = datetime.now().year
        if month <= 0:
            month += 12
            year -= 1
        return month, year
    
    def _add_month(self, df, month):
        months = ["January", "February", "March", "April", "May", "June", "August", "September", "October", "November", "December"]
        df["Month"] = months[month - 1]
        return df
    
    @abstractmethod
    def _get_month_summary(self, data, month: int, year: int):
        pass