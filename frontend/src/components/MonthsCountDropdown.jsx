import { useState } from "react";
import './MonthsCountDropdown.css'

export default function MonthCountDropdown(){
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className="dropdown">
            <button onClick={() => setIsOpen(!isOpen)}>
                Months ▼
            </button>
            {isOpen && (
                <div className="dropdown-content">
                    {/* Send request to API */}
                    <button>3</button> 
                    <button>4</button>
                </div>
            )}
        </div>
    )
}