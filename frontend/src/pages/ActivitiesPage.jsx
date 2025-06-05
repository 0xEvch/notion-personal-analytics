import React, { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import './ActivitiesPage.css';
import BarChart from '../components/charts/BarChart';

const fetchCharts = async (chartConfigs, selectedMonths, setError) => {
    try {
      const requests = chartConfigs.map(({ endpoint, setChart }) =>
        axios.get(`http://127.0.0.1:8000/${endpoint}?months_back=${selectedMonths}`).then(
          (response) => {
            setChart(response);
          }
        )
      );
      await Promise.all(requests);
      setError(null);
    } catch (err) {
      setError('Ошибка при загрузке данных с сервера');
      console.error(err);
    }
};

export default function ActivitiesPage({ selectedMonths }) {
    const [timeByActivity, setTimeByActivity] = useState(null);
    const [uniqueDaysByActivity, setUniqueDaysByActivity] = useState(null);
    const [totalTime, setTotalTime] = useState(null);
    const [totalUniqueDays, setTotalUniqueDays] = useState(null);
    const [error, setError] = useState(null);

    const chartConfigs = React.useMemo(() => [
        { endpoint: 'activities/time_by_month', setChart: setTimeByActivity },
        { endpoint: 'activities/unique_days_by_month', setChart: setUniqueDaysByActivity },
        { endpoint: 'activities/total_time_by_month', setChart: setTotalTime },
        { endpoint: 'activities/total_unique_days_by_month', setChart: setTotalUniqueDays },
    ], []);

    useEffect(() => {
        fetchCharts(chartConfigs, selectedMonths, setError);
    }, [selectedMonths]);
    
    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div className="charts-column">
        <div className="content-wrapper">
            <div className="big-block">
                {timeByActivity ? (
                    <BarChart chartData={timeByActivity} />
                ) : ('Loading...')}
            </div>
            <div className="medium-blocks">
            <div className="medium-block">
                {totalTime ? (
                    <BarChart chartData={totalTime} />
                ) : ('Loading...')}
            </div>
            <div className="medium-block">
                {totalUniqueDays ? (
                    <BarChart chartData={totalUniqueDays} />
                ) : ('Loading...')}
            </div>
            </div>
            <div className="small-blocks">test</div>
        </div>
        </div>
    );
}