import pandas as pd
from core.services.base_summary import Summary

class ActivitySummary(Summary):    
    def get_activity_time_by_month(self, data, months_back, include_this_month):
        result = self._collect_monthly_summaries(data, months_back, include_this_month, "activity_type")
        result = self._get_correct_month_order(result)
        return self._pivot_data(result, "Total Time", "Month")
    
    def get_activity_unique_days_by_month(self, data, months_back, include_this_month):
        result = self._collect_monthly_summaries(data, months_back, include_this_month, "activity_type")
        result = self._get_correct_month_order(result)
        return self._pivot_data(result, "Unique Days", "Month").astype('Int64')
    
    def get_total_time_by_month(self, data, months_back, include_this_month):
        result = self._aggregate_metrics_by_month(data, months_back, include_this_month, 'Total Time')
        return result['Total Time']

    def get_total_unique_days_for_month(self, data, months_back, include_this_month):
        result = self._aggregate_metrics_by_month(data, months_back, include_this_month, 'Unique Days')
        return result['Unique Days']
    
    def get_top_three_categories_by_month(self, data, months_back, include_this_month):
        categories = self._collect_monthly_summaries(data, months_back, include_this_month, "activity_type")
        categories_total = categories.groupby('Month').apply(
            lambda df: df.sort_values(by='Total Time (min)', ascending=False).head(3)
        )
        categories_sorted = categories_total.sort_values(by='Order',  ascending=False)
        return categories_sorted[['Total Time (min)', 'Total Time']]

    def get_top_three_activities_by_month(self, data, months_back, include_this_month):
        activities = self._collect_monthly_summaries(data, months_back, include_this_month, "name")
        activities_total = activities.groupby('Month').apply(
            lambda df: df.sort_values(by='Total Time (min)', ascending=False).head(3)
        )
        activities_sorted = activities_total.sort_values(by='Order',  ascending=False)
        return activities_sorted[['Total Time (min)', 'Total Time']]

    def get_average_time_per_day(self, data, months_back, include_this_month):  
        summary = self._collect_monthly_summaries(data, months_back, include_this_month, 'date')
        result = summary.groupby('Month').apply(
            lambda df: (df.sum() / df.count()).round(1)
            )
        sorted = result.sort_values(by='Order')
        return sorted[['Total Time (min)', 'Total Time']]

    def get_most_active_month(self, data):
        summary = self._collect_monthly_summaries(data, 12, False, 'activity_type')
        result = self._get_correct_month_order(summary)
        theMostActiveMonth = result.groupby('Month').agg({
            'Month': 'first',
            'Total Time (min)': 'sum',
            'Total Time': 'sum',
            'Unique Days' :'sum'
        }).max()
        return theMostActiveMonth
    
    def _aggregate_metrics_by_month(self, data, months_back, include_this_month, column_to_sum):
        data = self._collect_monthly_summaries(data, months_back, include_this_month, "date")
        return data.groupby('Month').agg({
            column_to_sum: 'sum',
            'Order': 'first'
        }).sort_values(by='Order', ascending=False)
    
    def _collect_monthly_summaries(self, data, months_back: int, include_this_month: bool, group_by: str):
        summaries = []
        for offset in range(months_back):
            month, year = self._get_month_by_offset(offset, include_this_month)
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