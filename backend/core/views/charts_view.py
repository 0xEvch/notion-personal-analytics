import matplotlib.pyplot as plt
import seaborn as sns  
# import mplcursors
# import base64
# import io

class BaseChartView:
    def __init__(self):
        self.colors = sns.color_palette("pastel")
    
    def _create_barchart(self, summary, figsize):
        fig, ax = plt.subplots(figsize=figsize)
        summary.plot(
            kind='bar',
            ax=ax,
            color=self.colors,
            alpha=0.8
        )
        self._configure_plot(ax)
    
    def _configure_plot(self, ax):
        plt.xlabel(None)
        ax.grid(axis='y', linestyle='--', alpha=0.5)
        ax.grid(axis='x', linestyle='--', alpha=0.3)

    def _save_to_base64(self):
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()
        return img_base64
    
    # def _add_interactive_cursor(self, ax):
    #     cursor = mplcursors.cursor(ax, hover=True)
        
    #     @cursor.connect("add")
    #     def on_add(sel):
    #         index = sel.index
    #         bar = sel.artist[index]
    #         value = bar.get_height()
    #         sel.annotation.set_text(f'{value:.2f} hours')
    #         sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9)

    # def show_chart(self, ax):
    #     self._add_interactive_cursor(ax)
    #     cursor.connect("add", lambda sel: sel.annotation.get_bbox_patch().set(fc="white", alpha=0.9))

    #     plt.tight_layout()
    #     plt.show()