import React, { useState } from 'react';
import ActivitiesPage from './ActivitiesPage';
import FinancesPage from './FinancesPage';
import MonthsCountDropdown from '../components/MonthsCountDropdown';
import './MainPage.css';

export default function MainPage ({ selectedTable }) {
  const [selectedMonths, setSelectedMonths] = useState(3);

  const getContent = () => {
    switch (selectedTable) {
      case 'activities':
        return <ActivitiesPage selectedMonths={selectedMonths} />;
      case 'finances':
        return <FinancesPage selectedMonths={selectedMonths} />;
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
      <div className="content-section">{getContent()}</div>
    </div>
  );
};