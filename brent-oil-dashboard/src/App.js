import React from 'react';
import Dashboard from './dashboard'; // Ensure this path is correct based on your folder structure
import './App.css'; // Import the CSS for styling

const App = () => {
    return (
        <div className="app-container">
            <h1>Brent Oil Prices Dashboard</h1>
            <Dashboard />
        </div>
    );
};

export default App;