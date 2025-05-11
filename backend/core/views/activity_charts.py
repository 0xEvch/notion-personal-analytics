import matplotlib.pyplot as plt
import seaborn as sns  
from core.views.charts_view import BaseChartView

class ActivityChartView(BaseChartView):
    def get_bar_chart_by_activity_type(self, summary):
            self._create_bar_chart(summary)
            img = self._save_to_base64
            return img