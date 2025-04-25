import matplotlib.pyplot as plt
import seaborn as sns  
import mplcursors

class Histogram:
    def create_chart(self, summary):
        month_order = ["January", "February", "March", "April", "May", "June", "August", "September", "October", "November", "December"]

        pivot_data = summary.pivot(
            index='Activity Type', columns='Month', values='Total Time'
            ).fillna(0)
        
        pivot_data = pivot_data[[col for col in month_order if col in pivot_data.columns]]
        
        colors = sns.color_palette("pastel", len(pivot_data.columns))

        ax = pivot_data.plot(
            kind='bar', 
            figsize=(12, 6), 
            color=colors,
            alpha=0.8 
        )

        plt.title('Total Time Comparison by Activity Type', fontsize=14, pad=15)
        plt.ylabel('Total Time (hours)', fontsize=12)
        plt.xlabel('Activity Type', fontsize=12)
        plt.xticks(rotation=45, ha='right') 
        plt.legend(title='Month', fontsize=10)

        cursor = mplcursors.cursor(ax, hover=True)
        @cursor.connect("add")
        def on_add(sel):
            index = sel.index
            bar = sel.artist[index]
            value = bar.get_height()
            sel.annotation.set_text(f'{value:.2f} hours')

        cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9))

        plt.tight_layout()
        plt.show()