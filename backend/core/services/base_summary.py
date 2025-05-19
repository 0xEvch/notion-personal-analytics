from datetime import datetime
import pandas as pd

class Summary():
    def get_json(self, df: pd.DataFrame) -> str:
        return df.to_json(orient="records", lines=True)
    
    def _pivot_data(self, data, values, columns):
        return data.pivot_table(
            index = data.index,
            values = values,
            columns = columns,
            fill_value = 0,
            observed=False
        )
    
    def _get_correct_month_order(self, data):
        all_months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]

        unique_months = data["Month"].unique()
        ordered_months = [month for month in all_months if month in unique_months]

        data["Month"] = pd.Categorical(data["Month"], categories=ordered_months, ordered=True)

        return data
    
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