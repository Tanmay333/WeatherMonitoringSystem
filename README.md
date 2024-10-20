Real-Time Weather Monitoring System
Overview
This project is a Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates, which retrieves real-time weather data from the OpenWeatherMap API for major Indian cities. The system provides weather summaries and stores data in a CSV file.

Features
Fetches real-time weather data for Delhi, Mumbai, Chennai, Bengaluru, Kolkata, and Hyderabad.
Converts temperature from Kelvin to Celsius.
Stores weather data in CSV format and allows for basic storage and retrieval of weather data.
Includes daily weather summaries such as:
Average, maximum, and minimum temperatures.
Dominant weather condition.
CSV storage for future analysis.
Supports user-configurable temperature thresholds to trigger alerts if a specified threshold is exceeded.

Getting Started
Prerequisites
Before running the application, ensure you have the following installed:

Python 3.x
SQLite3 (if you plan to use the database feature in the future)
Git

Design Choices
Real-time data fetching: The system continuously fetches weather data every 5 minutes to provide updated information.
CSV storage: Weather data is stored in a CSV file for easy access and analysis.
Threshold Alerts: Allows setting temperature thresholds to trigger alerts in case of high temperatures.
Future Enhancements
SQLite Database: Although this project currently focuses on CSV storage, it is set up for future use with SQLite for more persistent data storage.
Visualizations: The system can be extended to provide visual representations of historical weather trends.
