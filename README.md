# Phonepe_DataVisualization
Interactive dashboard to visualize PhonePe Pulse data using Streamlit, MySQL, and Plotly. Features 2D maps and charts showing top states, districts, and pincodes based on transactions, users, and app activity. Includes mobile brand analytics and overall quarterly rankings.
# 📱 PhonePe Pulse Data Visualization Dashboard

An interactive analytics dashboard built using **Streamlit**, **MySQL**, and **Plotly** to explore and visualize PhonePe Pulse data. The project features real-time insights with 3D maps, charts, and filters based on transactions, users, and device metrics.

## 🔍 Features

- 📈 Overall rankings by year and quarter.
- 🏆 Top 10 States, Districts, and Pincodes based on:
  - Total number of transactions
  - Total transaction amount
- 👥 Top 10 locations by:
  - PhonePe users
  - App opening frequency
- 📱 Top 10 mobile brands and user distribution.
- 🗺️ 3D Choropleth map of India with bar plots for visual depth.
- 💾 Backend powered by MySQL for optimized queries.

## 🛠 Tech Stack

- Frontend: **Streamlit**
- Backend: **Python**
- Database: **MySQL**
- Visualization: **Plotly 2D**
- Deployment Ready

## 🚀 Getting Started

1. Clone the repository
2. Set up MySQL database with PhonePe data
3. Run the Streamlit app

```bash
streamlit run app.py
