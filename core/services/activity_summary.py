import pandas as pd
from datetime import datetime
from dataclasses import asdict
from data.notion.sync_manager import SyncManager

class ActivitySummary:
    @staticmethod
    def get_three_month_activity_statistics():
        data = ActivitySummary._create_dataframe()
        this_month = ActivitySummary._get_month(0)
        prev_month = ActivitySummary._get_month(1)
        prev_2_months = ActivitySummary._get_month(2)

        this_month_summary = ActivitySummary._get_month_summary(data, this_month[0], this_month[1])
        prev_month_summary = ActivitySummary._get_month_summary(data, prev_month[0], prev_month[1])
        prev_2_months_summary = ActivitySummary._get_month_summary(data, prev_2_months[0], prev_2_months[1])

        return (this_month_summary, prev_month_summary, prev_2_months_summary)

    @staticmethod
    def _create_dataframe():
        data = SyncManager.get_autopilot_data()
        df = pd.DataFrame([asdict(item) for item in data])
        df['date'] = pd.to_datetime(df['date'])
        return df
    
    @staticmethod
    def _get_month_summary(df, month, year):
        month_filter = df[(df['date'].dt.month == month) & (df['date'].dt.year == year)]
        month_summary = month_filter.groupby("activity_type").agg({
            'duration_min': 'sum',
            'date': 'nunique'
        }).rename(columns={'duration_min': 'Total Time (min)', 'date': 'Unique Days'})
        return month_summary
    
    @staticmethod
    def _get_month(offset):
        month = datetime.now().month
        year = datetime.now().year
        
        if month == offset:
            month = 12
            year -= 1
        elif month < offset:
            diff = offset - month
            month = 12 - diff
            year -= 1
        elif 0 < offset <= 12:
            month -= offset
        return (month, year)

if __name__ == "__main__":
    print(ActivitySummary.get_three_month_activity_statistics())