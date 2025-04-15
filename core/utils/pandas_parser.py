import pandas as pd
from dataclasses import asdict

class PandasParser:
    def get_dataframe(data):
        df = pd.DataFrame([asdict(item) for item in data])
        df['date'] = pd.to_datetime(df['date'])
        return df