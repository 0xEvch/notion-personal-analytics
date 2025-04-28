import matplotlib.pyplot as plt
import seaborn as sns  
import mplcursors
import base64
import io

class Histogram:
    def __init__(self):
        self.month_order = ["January", "February", "March", "April", "May", "June", "August", "September", "October", "November", "December"]
        self.figsize = (12, 6)
        self.colors = sns.color_palette("pastel")

    def get_chart(self, summary):
        self._create_chart(summary)
        img = self._save_to_base64
        return img
    
    def _create_chart(self, summary):
        pivot_data = self._prepare_data(summary)
        
        fig, ax = plt.subplots(figsize=self.figsize)
        pivot_data.plot(
            kind='bar',
            ax=ax,
            color=self.colors[:len(pivot_data.columns)],
            alpha=0.8
        )

        self._configure_plot(ax)
    
    def _prepare_data(self, summary):
        pivot_data = summary.pivot(
            index='Activity Type', 
            columns='Month', 
            values='Total Time'
        ).fillna(0)
        return pivot_data[[col for col in self.month_order if col in pivot_data.columns]]
    
    def _configure_plot(self, ax):
        plt.title('Total Time Comparison by Activity Type', fontsize=14, pad=15)
        plt.ylabel('Total Time (hours)', fontsize=12)
        plt.xlabel('Activity Type', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.legend(title='Month', fontsize=10)
        plt.tight_layout()

    def _save_to_base64(self):
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()
        return img_base64
    
    def _add_interactive_cursor(self, ax):
        cursor = mplcursors.cursor(ax, hover=True)
        
        @cursor.connect("add")
        def on_add(sel):
            index = sel.index
            bar = sel.artist[index]
            value = bar.get_height()
            sel.annotation.set_text(f'{value:.2f} hours')
            sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9)

    # def show_chart(self, ax):
    #     self._add_interactive_cursor(ax)
    #     cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9))

    #     plt.tight_layout()
    #     plt.show()