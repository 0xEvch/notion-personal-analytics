from abc import ABC, abstractmethod
from datetime import datetime
import pandas as pd

class Summary(ABC):
    def get_json(self, df: pd.DataFrame) -> str:
        return df.to_json(orient="records", lines=True)
    
    def _get_month_by_offset(self, offset: int):
        month = datetime.now().month - offset
        year = datetime.now().year
        if month <= 0:
            month += 12
            year -= 1
        return month, year
    
    def _add_month_name(self, df, month):
        months = ["January", "February", "March", "April", "May", "June", "August", "September", "October", "November", "December"]
        df["Month"] = months[month - 1]
        return df
    
    def _filter_by_month(self, df, month, year):
        return df[(df['date'].dt.month == month) & (df['date'].dt.year == year)] 