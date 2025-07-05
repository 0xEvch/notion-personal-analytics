import React, { useState } from 'react';
import './IncludeThisMonthButton.css';

const IncludeThisMonthButton = ({ includeThisMonth, setIncludeThisMonth }) => {
    return (
        <div className="toggle-wrapper">
            <span className="toggle-label">Include this month</span>
            <div className="toggle-container">
                <button 
                    className={`toggle-switch ${includeThisMonth ? 'active' : ''}`}
                    onClick={() => setIncludeThisMonth(prev => !prev)}
                    aria-label={includeThisMonth ? 'Исключить текущий месяц, активный' : 'Включить текущий месяц, неактивный'}
                >
                    <div className="toggle-knob">{includeThisMonth ? 'YES' : 'NO'}</div>
                </button>
            </div>
        </div>
    );
};

export default IncludeThisMonthButton;