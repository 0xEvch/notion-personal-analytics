import Plotly from 'plotly.js-dist-min';
import { useEffect, useRef } from 'react';

const TimeBarChart = ({ chartData }) => {
  const chartRef = useRef(null);

  const pastelColors = [
    '#AEC6CF', '#FFB7B2', '#B2DFDB', '#F0B7DA', '#C1E1C1',
  ];

  useEffect(() => {
    if (!chartData || !chartRef.current) return;

    console.log('chartData:', chartData);

    // Проверяем структуру chartData и извлекаем данные
    let parsedData;
    try {
      // Если chartData.data — строка, парсим её
      const dataToParse = chartData.data || chartData;
      parsedData = typeof dataToParse === 'string' ? JSON.parse(dataToParse) : dataToParse;

      // Если chartData.data уже объект
      if (parsedData.data) {
        parsedData = typeof parsedData.data === 'string' ? JSON.parse(parsedData.data) : parsedData.data;
      }
    } catch (err) {
      return;
    }

    // Извлекаем активности и месяцы
    const activities = Object.keys(parsedData);
    const months = Object.keys(parsedData[activities[0]]); // Берем месяцы из первой активности

    // Формируем данные для Plotly
    const plotData = months.map((month, index) => {
      const trace = {
        x: activities, // Активности на оси X
        y: activities.map((activity) => parsedData[activity][month] || 0), // Значения для месяца
        type: 'bar',
        name: month, // Название месяца для легенды
        marker: {
          color: pastelColors[index % pastelColors.length], // Пастельные цвета
          opacity: 0.8,
        },
      };
      console.log(`Trace for ${month}:`, trace);
      return trace;
    });

    // Настройки графика
    const layout = {
      title: {
        text: chartData.title || 'Total Time comparison by Activity Type',
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
          text: chartData.ylabel || 'Total Time (hours)',
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
      showlegend: true,
      plot_bgcolor: 'rgba(0,0,0,0)', // Прозрачный фон
      paper_bgcolor: 'rgba(0,0,0,0)', // Прозрачный фон бумаги
      margin: { t: 60, b: 60, l: 60, r: 40 }, // Компактные отступы
    };

    console.log('plotData:', plotData);
    console.log('layout:', layout);

    Plotly.newPlot(chartRef.current, plotData, layout, { responsive: true });

    return () => {
      if (chartRef.current) {
        Plotly.purge(chartRef.current); // Очистка при размонтировании
      }
    };
  }, [chartData]);

  return <div ref={chartRef} style={{ width: '100%', height: '500px' }} />;
};

export default TimeBarChart;