import matplotlib.pyplot as plt
import seaborn as sns  
from core.views.charts_view import BaseChartView

class ActivityChartView(BaseChartView):
    def get_time_barchart(self, data):       
        figsize = (12, 5) 
        self._create_barchart(data, figsize)

        plt.title('Total Time comparison by Activity Type', fontsize=12, pad=15)
        plt.ylabel('Total Time (hours)', fontsize=12)
        plt.xticks(rotation=-20, ha='left')
        plt.legend(title='Month', fontsize=10)      
        plt.tight_layout()

        img = self._save_to_base64
        return img
    
    def get_unique_days_barchart(self, data):
        figsize = (12, 5)
        self._create_barchart(data, figsize)

        plt.title('Unique days comparison by Activity Type', fontsize=12, pad=15)
        plt.ylabel('Days', fontsize=12)
        plt.xticks(rotation=-20, ha='left')
        plt.legend(title='Month', fontsize=10)      
        plt.tight_layout()

        img = self._save_to_base64
        return img