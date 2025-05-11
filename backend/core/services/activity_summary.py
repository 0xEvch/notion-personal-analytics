import pandas as pd
from core.services.base_summary import Summary

class ActivitySummary(Summary):    
    def get_total_time_table_view_by_type(self, data, months_back):
        result = self._get_raw_summary_for_n_months(data, months_back)
        return self._pivot_data(result, "Total Time", "Month")
    
    def get_unique_days_table_view_by_type(self, data, months_back):
        result = self._get_raw_summary_for_n_months(data, months_back)
        return self._pivot_data(result, "Unique Days", "Month").astype('Int64')
    
    def get_total_time_for_month(self, data, months_back):
        month, year = self._get_month_by_offset(months_back)
        data = self._filter_by_month(data, month, year)
        amount = data['duration_min'].sum()
        return amount

    def get_unique_days_for_month(self, data, months_back):
        month, year = self._get_month_by_offset(months_back)
        data = self._filter_by_month(data, month, year)
        uniq_days = len(data['date'].unique())
        return uniq_days
    
    def _get_raw_summary_for_n_months(self, data, months_back: int):
        summaries = []
        for offset in range(months_back):
            month, year = self._get_month_by_offset(offset)
            summary = self._get_month_summary_by_type(data, month, year)
            summary = self._add_month_name(summary, month)
            summaries.append(summary)
        return pd.concat(summaries, ignore_index=False)
    
    def _get_month_summary_by_type(self, data, month, year):
        data = self._filter_by_month(data, month, year)
        month_summary = data.groupby("activity_type", as_index=True).agg({
            'duration_min': 'sum',
            'duration_hrs': 'sum',
            'date': 'nunique'
        }).rename(columns={
            'duration_min': 'Total Time (min)', 
            'duration_hrs': 'Total Time',
            'date': 'Unique Days'
            })
        
        month_summary.index.name = 'Activity Type'

        return month_summary

if __name__ == "__main__":
    autopilot = ActivitySummary()
    
    print(autopilot._get_month_summary_by_type(3))