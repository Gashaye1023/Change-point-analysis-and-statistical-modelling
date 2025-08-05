import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [data, setData] = useState({});

    useEffect(() => {
        axios.get('/api/change_points')
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Brent Oil Price Change Point Analysis</h1>
            <h2>Estimated Change Point: {data.change_point}</h2>
            <h3>Average Log Return Before Change: {data.average_before}</h3>
            <h3>Average Log Return After Change: {data.average_after}</h3>
        </div>
    );
};

export default Dashboard;