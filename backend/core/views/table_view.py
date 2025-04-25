import matplotlib.pyplot as plt
from matplotlib.table import Table
import seaborn as sns

class Tables:
    def create_hours_table(self, summary):
        pivot = summary.pivot_table(
            index='Activity Type',
            columns='Month',
            values='Total Time (min)',
            fill_value=0
        )

        pivot.loc['Total'] = pivot.sum()

        pivot = self._sort_month_order(pivot)

        self._plot_table(pivot, 'Total Time by Activity Type and Month')

    def create_unique_days_table(self, summary):
        pivot = summary.pivot_table(
            index='Activity Type',
            columns='Month',
            values='Unique Days',
            fill_value=0
        )

        pivot.loc['Total'] = pivot.sum()

        pivot = self._sort_month_order(pivot)

        self._plot_table(pivot, 'Unique Days by Activity Type and Month')

    def _sort_month_order(self, data):
        month_order = ["January", "February", "March", "April", "May", "June", "August", "September", "October", "November", "December"]
        data = data.reindex(columns=month_order, fill_value=0)
        data = data.loc[:, (data != 0).any(axis=0)]
        return data

    def _plot_table(self, pivot_data, title):
        fig, ax = plt.subplots(figsize=(8, len(pivot_data) * 0.5 + 1))
        ax.axis('off') 

        table = Table(ax, bbox=[0, 0, 1, 1])

        n_rows, n_cols = pivot_data.shape
        header_color = "#D3D3D3"

        for j, col in enumerate(pivot_data.columns):
            table.add_cell(0, j + 1, 1, 1, text=col, loc='center', facecolor=header_color)

        for i, row in enumerate(pivot_data.index):
            if i < len(pivot_data.index) - 1:
                table.add_cell(i + 1, 0, 1, 1, text=row, loc='center')
            else:
                table.add_cell(i + 1, 0, 1, 1, text=row, loc='center', facecolor=header_color)

        for i in range(n_rows):
            for j in range(n_cols):
                value = pivot_data.iloc[i, j]
                text = f'{int(value)}'
                if i < len(pivot_data.index) - 1:
                    table.add_cell(i + 1, j + 1, 1, 1, text=text, loc='center')
                else:
                    table.add_cell(i + 1, j + 1, 1, 1, text=text, loc='center', facecolor=header_color)

        ax.add_table(table)

        plt.title(title, fontsize=14, pad=20)

        plt.tight_layout()
        plt.show()