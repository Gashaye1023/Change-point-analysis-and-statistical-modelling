# Change point analysis and statistical modelling of time series data - detecting changes and associating causes on time series data
### Steps and Methodology

#### 1. Business Objective
The main goal is to analyze how key events affect Brent oil prices. This includes understanding the impact of political decisions, conflicts, economic sanctions, and OPEC policies on oil prices, providing actionable insights for investors, analysts, and policymakers.

#### 2. Situational Overview
As a data scientist at Birhan Energies, you need to provide detailed analyses to help stakeholders navigate the complexities of the oil market, which is often volatile and influenced by various external factors.

#### 3. Data Collection
- **Dataset**: Historical Brent oil prices from May 20, 1987, to September 30, 2022.
- **Data Fields**: 
  - Date (formatted as ‘day-month-year’)
  - Price (recorded in USD per barrel)

### Methodology

#### Task 1: Laying the Foundation for Analysis

1. **Defining the Data Analysis Workflow**
   - Outline the steps involved in analyzing Brent oil prices.
   - Research and compile a dataset of key geopolitical events, including dates.

2. **Understanding the Model and Data**
   - Analyze the time series properties of Brent oil prices (trends, stationarity).
   - Discuss the purpose of change point models in identifying structural breaks in the data.

#### Task 2: Change Point Modeling and Insight Generation

1. **Data Preparation and Exploration**
   - Load the data and convert the Date column to datetime format.
   - Plot the raw price series to identify trends and shocks.
   - Analyze log returns to ensure stationarity for modeling.

2. **Implementing the Change Point Model**
   - **Define the Switch Point (tau)**: Use a discrete uniform prior for potential change points.
   - **Define Parameters**: Establish parameters for behavior before and after the change point.
   - **Likelihood Definition**: Use a normal distribution to connect the model to the observed data.
   - **Sampling**: Run MCMC simulations to obtain posterior distributions of parameters.

3. **Interpreting Model Output**
   - Check convergence and analyze trace plots.
   - Identify change points and quantify their impacts by comparing price shifts associated with key events.

#### Task 3: Developing an Interactive Dashboard

1. **Backend Development (Flask)**
   - Create APIs to serve analysis results.
   - Handle requests for datasets and model outputs.

2. **Frontend Development (React)**
   - Build a user-friendly interface for visualizing results.
   - Implement interactive charts and filters to explore data related to specific events.

3. **Key Features of the Dashboard**
   - Present historical trends and correlations with significant events.
   - Include functionality for users to filter data and analyze specific time periods.
   - Display key indicators such as volatility and average price changes.
