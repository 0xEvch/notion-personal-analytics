import pandas as pd
from core.services.base_summary import Summary

class ActivitySummary(Summary):    
    def get_total_time_table_view_by_type(self, data, months_back):
        result = self._get_raw_summary_for_n_months(data, months_back, "activity_type")
        result = self._get_correct_month_order(result)
        return self._pivot_data(result, "Total Time", "Month")
    
    def get_unique_days_table_view_by_type(self, data, months_back):
        result = self._get_raw_summary_for_n_months(data, months_back, "activity_type")
        result = self._get_correct_month_order(result)
        return self._pivot_data(result, "Unique Days", "Month").astype('Int64')
    
    def get_total_time_for_month(self, data, months_back):
        result = self._get_raw_total_for_n_months(data, months_back, 'Total Time')
        return result['Total Time']

    def get_unique_days_for_month(self, data, months_back):
        result = self._get_raw_total_for_n_months(data, months_back, 'Unique Days')
        return result['Unique Days']
    
    def _get_raw_total_for_n_months(self, data, months_back, column_to_sum):
        data = self._get_raw_summary_for_n_months(data, months_back, "date")
        return data.groupby('Month').agg({
            column_to_sum: 'sum',
            'Order': 'first'
        }).sort_values(by='Order', ascending=False)
    
    def _get_raw_summary_for_n_months(self, data, months_back: int, group_by: str):
        summaries = []
        for offset in range(months_back):
            month, year = self._get_month_by_offset(offset)
            summary = self._get_month_summary_by_type(data, month, year, group_by)
            summary = self._add_month_name(summary, month)
            summary['Order'] = offset
            summaries.append(summary)
        return pd.concat(summaries, ignore_index=False)
    
    def _get_month_summary_by_type(self, data, month, year, group_by):
        data = self._filter_by_month(data, month, year)
        month_summary = data.groupby(group_by, as_index=True).agg({
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