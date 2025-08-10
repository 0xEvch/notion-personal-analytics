import React, { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import './ActivitiesPage.css';
import BarChart from '../components/charts/BarChart';
import Table from '../components/views/TableView';
import TopThreeActicities from '../components/views/TopThreeActicities'
import TheMostActiveMonth from '../components/views/TheMostActiveMonth'

const fetchCharts = async (chartConfigs, selectedMonths, includeThisMonth, setError) => {
    try {
      const requests = chartConfigs.map(({ endpoint, setChart }) =>
        axios.get(`http://127.0.0.1:8000/${endpoint}?months_back=${selectedMonths}&include_this_month=${includeThisMonth}`).then(
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

export default function ActivitiesPage({ selectedMonths, includeThisMonth }) {
    const [timeByActivity, setTimeByActivity] = useState(null);
    const [uniqueDaysByActivity, setUniqueDaysByActivity] = useState(null);
    const [totalTime, setTotalTime] = useState(null);
    const [totalUniqueDays, setTotalUniqueDays] = useState(null);
    const [topThree, setTopThree] = useState (null);
    const [avgTimePerDay, setAvgTimePerDay] = useState(null);
    const [mostActiveMonth, setMostActiveMonth] = useState(null);
    const [error, setError] = useState(null);

    const chartConfigs = React.useMemo(() => [
        { endpoint: 'activities/time_by_month', setChart: setTimeByActivity },
        { endpoint: 'activities/unique_days_by_month', setChart: setUniqueDaysByActivity },
        { endpoint: 'activities/total_time_by_month', setChart: setTotalTime },
        { endpoint: 'activities/total_unique_days_by_month', setChart: setTotalUniqueDays },
        { endpoint: 'activities/top_three', setChart: setTopThree },
        { endpoint: 'activities/average_time_per_day', setChart: setAvgTimePerDay },
        { endpoint: 'activities/the_most_active_month', setChart: setMostActiveMonth },
    ], []);

    useEffect(() => {
        fetchCharts(chartConfigs, selectedMonths, includeThisMonth, setError);
    }, [selectedMonths, includeThisMonth]);
    
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
            <div className="small-blocks">
            <div className="small-block">
                {topThree ? (
                    <Table data={topThree} />
                ) : ('Loading...')}
            </div>  
            <div className="small-block">
                {avgTimePerDay ? (
                    <Table data={avgTimePerDay} />
                ) : ('Loading...')}
            </div>  
            </div>
        </div>
        <div className="right-column">
            <div>
                {mostActiveMonth ? (
                    <TheMostActiveMonth data={mostActiveMonth} />
                ) : ('Loading...')}
            </div>
            <div>
                {topThree ? (
                    <TopThreeActicities data={topThree} />
                ) : ('Loading...')}
            </div>
        </div>
        </div>
    );
}