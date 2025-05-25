import logo from './logo.svg';
import './App.css';
import Sidebar from './components/SideBar.jsx'
import MainPage from './pages/MainPage';
import { useState } from 'react';

function App() {
  const [isSidebarOpen, setIsOpen] = useState(false);
  const [selectedTable, setSelectedTable] = useState('activities');

  return (
    <div className="app-container">
      <Sidebar 
        isOpen={isSidebarOpen}
        setIsOpen={setIsOpen}
        selectedTable={selectedTable}
        setSelectedTable={setSelectedTable}
      />
      <MainPage selectedTable={selectedTable} />
    </div>
  );
}

export default App;
