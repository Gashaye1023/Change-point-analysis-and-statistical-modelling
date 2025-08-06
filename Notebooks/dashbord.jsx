import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';

const Dashboard = () => {
    const [data, setData] = useState([]);
    const [changePoints, setChangePoints] = useState({});
    const [events, setEvents] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const priceData = await axios.get('/api/historical_data');
            const changePointData = await axios.get('/api/change_points');
            const eventData = await axios.get('/api/events');

            setData(priceData.data);
            setChangePoints(changePointData.data);
            setEvents(eventData.data);
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>Brent Oil Prices Dashboard</h1>
            <LineChart width={600} height={300} data={data}>
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="price" stroke="#8884d8" />
            </LineChart>
            <div>
                <h2>Change Points</h2>
                <p>Change Point: {changePoints.change_point}</p>
                <p>Average Before: {changePoints.average_before}</p>
                <p>Average After: {changePoints.average_after}</p>
            </div>
            <div>
                <h2>Events</h2>
                <ul>
                    {events.map(event => (
                        <li key={event.date}>{event.date}: {event.event} - {event.description}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Dashboard;
