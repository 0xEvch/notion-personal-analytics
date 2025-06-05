import React, { Component } from 'react';
import Plotly from 'plotly.js-dist-min';

class BarChart extends Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
    this.pastelColors = [
      '#AEC6CF', '#FFB7B2', '#B2DFDB', '#F0B7DA', '#C1E1C1',
    ];
  }

  parseChartData(chartData) {
    if (!chartData || !this.chartRef.current) return;

    try {
      // Если chartData.data — строка, парсим её
      const dataToParse = chartData.data || chartData;
      let parsedData = typeof dataToParse === 'string' ? JSON.parse(dataToParse) : dataToParse;

      // Если chartData.data уже объект
      if (parsedData.data) {
        parsedData = typeof parsedData.data === 'string' ? JSON.parse(parsedData.data) : parsedData.data;
      }

      return parsedData;
    } catch (err) {
      console.error('Error parsing chartData:', err);
      return;
    }
  }

  extractActivitiesAndMonths(parsedData) {
    if (!parsedData) return { activities: [], months: [], isTotal: false };
    
    const keys = Object.keys(parsedData);
    // Извлекаем активности и месяцы
    if (keys.length > 0 && typeof parsedData[keys[0]] === 'object' && !Array.isArray(parsedData[keys[0]])) {
      const activities = keys;
      const months = Object.keys(parsedData[activities[0]] || {});
      return { activities, months, isTotal: false };
    } else {
      // Второй JSON: месяцы как ключи, значения — числа
      const months = keys;
      const activities = ['Total']; // Одна "активность" для отображения
      return { activities, months, isTotal: true };
    }
  }

  createPlotData(activities, months, parsedData, isTotal) {  
    if (isTotal) {
      // Для второго JSON: одна трасса с месяцами на оси X и значениями на оси Y
      return [{
        x: months,
        y: months.map(month => parsedData[month] || 0),
        type: 'bar',
        marker: {
          color: this.pastelColors[0],
          opacity: 0.8,
        },
      }];
    }
  // Формируем данные для Plotly
    return months.map((month, index) => {
      const trace = {
        x: activities, // Активности на оси X
        y: activities.map((activity) => parsedData[activity][month] || 0), // Значения для месяца
        type: 'bar',
        name: month, // Название месяца для легенды
        marker: {
          color: this.pastelColors[index % this.pastelColors.length], // Пастельные цвета
          opacity: 0.8,
        },
      };
      return trace;
    });
  }

  createLayout(chartData, isTotal) {
    // Настройки графика
    return {
      title: {
        text: chartData.data.title || '',
        font: { size: 12 },
        pad: { t: 15 },
      },
      xaxis: {
        title: null, // Без заголовка оси X
        tickangle: -20, // Поворот меток
        tickfont: { size: 10 },
        gridcolor: '#E5E5EF', // Сетка по X
        griddash: 'dot',
      },
      yaxis: {
        title: {
          text: chartData.data.ylabel || '',
          font: { size: 12 },
        },
        gridcolor: '#E5E5EF', // Сетка по Y
        griddash: 'dot',
        gridwidth: 1,
      },
      barmode: 'group', // Столбцы рядом
      legend: {
        title: { text: 'Month', font: { size: 10 } },
      },
      showlegend: !isTotal,
      plot_bgcolor: 'rgba(0,0,0,0)', // Прозрачный фон
      paper_bgcolor: 'rgba(0,0,0,0)', // Прозрачный фон бумаги
      margin: { t: 60, b: 60, l: 60, r: 40 }, // Компактные отступы
    };
  }

  renderChart() {
    const { chartData } = this.props;
    if (!chartData || !this.chartRef.current) return;

    const parsedData = this.parseChartData(chartData);
    if (!parsedData) return;

    const { activities, months, isTotal } = this.extractActivitiesAndMonths(parsedData);
    if (!activities.length || !months.length) return;
    console.log(chartData);
    
    const plotData = this.createPlotData(activities, months, parsedData, isTotal);
    const layout = this.createLayout(chartData, isTotal);

    Plotly.newPlot(this.chartRef.current, plotData, layout, { responsive: true });
  }

  cleanupChart() {
    if (this.chartRef.current) {
      Plotly.purge(this.chartRef.current);
    }
  }

  componentDidMount() {
    this.renderChart();
  }

  componentDidUpdate(prevProps) {
    if (prevProps.chartData !== this.props.chartData) {
      this.cleanupChart();
      this.renderChart();
    }
  }

  componentWillUnmount() {
    this.cleanupChart();
  }

  render() {
    return <div ref={this.chartRef} style={{ width: '100%', height: '500px' }} />;
  }
};

export default BarChart;