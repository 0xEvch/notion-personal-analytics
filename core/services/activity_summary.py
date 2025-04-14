import pandas as pd
from core.services.base_summary import Summary

class ActivitySummary(Summary):
    def _get_month_summary(self, month, year):
        month_filter = self.df[(self.df['date'].dt.month == month) & (self.df['date'].dt.year == year)]
        month_summary = month_filter.groupby("activity_type").agg({
            'duration_min': 'sum',
            'date': 'nunique'
        }).rename(columns={'duration_min': 'Total Time (min)', 'date': 'Unique Days'})
        return month_summary
    
if __name__ == "__main__":
    autopilot = ActivitySummary()
    
    print(autopilot.get_statistics(3))