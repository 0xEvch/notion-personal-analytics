import './SideBar.css'

export default function Sidebar({ isOpen, setIsOpen, selectedTable, setSelectedTable }){
    const menuItems = [
        { icon: '🕒', label: 'Activities', value: 'activities' },
        { icon: '🧾', label: 'Finances', value: 'finances' },
      ];
      
    return (
    <div
        className={`sidebar ${isOpen ? 'sidebar-open' : 'sidebar-closed'}`}
        onMouseEnter={() => setIsOpen(true)}
        onMouseLeave={() => setIsOpen(false)}
    >
        {menuItems.map((item, index) => (
        <div
            key={index}
            className={`sidebar-item ${selectedTable === item.value ? 'active' : ''}`}
            onClick={() => setSelectedTable(item.value)}
        >
            <span className="sidebar-icon">{item.icon}</span>
            {isOpen && <span className="sidebar-label">{item.label}</span>}
        </div>
        ))}
    </div>
    );
};