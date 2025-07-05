import React, { useState } from 'react';
import ActivitiesPage from './ActivitiesPage';
import FinancesPage from './FinancesPage';
import MonthsCountDropdown from '../components/MonthsCountDropdown';
import IncludeThisMonthButton from '../components/IncludeThisMonthButton';
import './MainPage.css';

export default function MainPage ({ selectedTable }) {
  const [selectedMonths, setSelectedMonths] = useState(3);
  const [includeThisMonth, setIncludeThisMonth] = useState(false);

  const getContent = () => {
    switch (selectedTable) {
      case 'activities':
        return <ActivitiesPage selectedMonths={selectedMonths} includeThisMonth={includeThisMonth} />;
      case 'finances':
        return <FinancesPage selectedMonths={selectedMonths} includeThisMonth={includeThisMonth}/>;
      default:
        return null;
    }
  };

  return (
    <div className="main-content">
      <MonthsCountDropdown
        selectedMonths={selectedMonths}
        onChange={setSelectedMonths}
      />
      <IncludeThisMonthButton 
        includeThisMonth={includeThisMonth}
        setIncludeThisMonth={setIncludeThisMonth}
      />
      <div className="content-section">{getContent()}</div>
    </div>
  );
};