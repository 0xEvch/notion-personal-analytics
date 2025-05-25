import React from 'react';
import './MonthsCountDropdown.css';

const MonthsCountDropdown = ({ selectedMonths, onChange }) => {
  const monthsOptions = [1, 3, 6, 12];

  return (
    <div className="dropdown-container">
      <button className="dropdown-button">
        {selectedMonths} {selectedMonths === 1 ? 'month' : 'months'}
      </button>
      <div className="dropdown-menu">
        {monthsOptions.map((month) => (
          <div
            key={month}
            className="dropdown-item"
            onClick={() => onChange(month)}
          >
            {month} {month === 1 ? 'month' : 'months'}
          </div>
        ))}
      </div>
    </div>
  );
};

export default MonthsCountDropdown;