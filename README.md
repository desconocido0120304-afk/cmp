# Eco-Track IoT Project

## Project Overview
Eco-Track is an innovative Internet of Things (IoT) project designed to monitor and manage environmental parameters. By utilizing various sensors, the system collects real-time data that helps in tracking ecological changes and improving sustainability efforts.

## What It Does
The Eco-Track system gathers data from multiple IoT sensors deployed in different environments. It processes this data through an AI component to provide insights into environmental conditions, facilitating smarter decision-making for conservation and sustainability.

## Key Features
- **Real-time Data Monitoring**: Continuous tracking of environmental parameters such as temperature, humidity, and air quality.
- **AI Integration**: Utilizes machine learning algorithms to analyze data and predict ecologically significant trends.
- **User-friendly Interfaces**: Offers both a desktop application and a web interface for user interaction.
- **Robust Database Structure**: Efficiently stores collected data for easy retrieval and analysis.

## How the IoT Sensors Work
The sensors are deployed across various locations and are responsible for capturing environmental data. They communicate with a central server via Wi-Fi or cellular networks, sending data at specified intervals. The data is then aggregated and processed for further analysis.

## The AI Component
The AI module analyzes the collected data using predictive algorithms. It helps identify trends and anomalies, providing users with actionable insights. The component is constantly updated with new data to improve accuracy and relevance.

## Database Structure
The project uses a relational database to manage the data collected from IoT sensors. The key tables include:
- **Users**: Stores user details and preferences.
- **Sensors**: Contains details about each sensor, including location and type.
- **Data**: Records the readings from sensors with time stamps.

## How to Set Up and Run the Application
1. Clone the repository using:
   ```bash
   git clone https://github.com/microsoft01cuenta-web/Proyecto-Comp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Proyecto-Comp
   ```
3. Install the required dependencies. For Python, use:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database according to the schema defined in the database migrations.
5. Run the application:
   - For the Python desktop app:
     ```bash
     python app.py
     ```
   - For the HTML web interface:
     Open `index.html` in a web browser.

## Project Structure
- `app.py`: Main entry point for the desktop application.
- `sensor`: Contains sensor-related modules.
- `ai_model`: Implements machine learning algorithms and models.
- `db`: Contains database setup and migration scripts.
- `web`: Contains HTML, CSS, and JavaScript files for the web interface.

## Instructions for the Python Desktop App
- Launch the application by running `app.py`. It provides a GUI to interact with the IoT data.
- Users can visualize real-time data, analyze trends, and access reports through the application.

## Instructions for the HTML Web Interface
- Open `index.html` in a web browser to access the web interface.
- The interface presents the same functionalities as the desktop app but in a web format.

## Conclusion
The Eco-Track project integrates cutting-edge technology to make environmental monitoring efficient and accessible. Through user-friendly interfaces and powerful AI analytics, this project aims to advance ecological sustainability initiatives.