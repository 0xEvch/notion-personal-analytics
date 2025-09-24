import React, { useState } from 'react';
import './TimeOrUnicDaysButton.css';

const TimeOrUnicDaysButton = ({ timeOrUnicDays, setTimeOrUnicDays }) => {
    return (
        <div className="toggle-wrapper-days">
            <span className="toggle-label">What total to display</span>
            <div className="toggle-container">
                <button 
                    className={`toggle-switch ${timeOrUnicDays ? 'active' : ''}`}
                    onClick={() => setTimeOrUnicDays(prev => !prev)}
                >
                    <div className="toggle-knob">{!timeOrUnicDays ? 'Time' : 'Unic days'}</div>
                </button>
            </div>
        </div>
    );
};

export default TimeOrUnicDaysButton;