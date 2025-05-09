# Home Project:  Efficient LED Farming System (Simulation Version)
<p align="center">
  <img src="https://github.com/user-attachments/assets/e6fc377a-653f-4ed5-a9fa-424069b0e919" style="width:60%;">
</p>

This project simulates an LED-based farming system with a Cloud-Based IoT approach, enabling dynamic light control, sensor monitoring, and real-time data visualization using cloud platforms.

## Overview
Urban agriculture and indoor farming face challenges related to natural light instability, fixed lighting inefficiencies, and high energy consumption. This project simulates a cloud-driven LED lighting system that dynamically adjusts red and blue wavelengths to optimize plant growth and efficiency.

## Features
- Dynamic LED Control: Simulated adjustment of red & blue LEDs for optimal plant growth stages.
- Sensor Data Simulation: Temperature & humidity data generation via Python scripts.
- Cloud-Based Data Storage: Uses InfluxDB for efficient logging of environmental conditions.
- Real-Time Visualization: Interactive Grafana dashboards displaying sensor trends & LED performance.
- Docker-Based Deployment: Simplified execution & version control using GitHub & Docker Compose.
<p align="center">
  <img src="https://github.com/user-attachments/assets/cc172fdc-8a05-438e-b0af-8af3dcca242a" style="width:50%;">
</p>

## System Components
The project consists of:
- Python Simulation Engine – Generates virtual sensor & LED data.
- InfluxDB Database – Stores simulated environmental conditions.
- Grafana Dashboard – Visualizes real-time system data.
- Docker & CI/CD – Ensures scalable, repeatable deployments.
![image](https://github.com/user-attachments/assets/adba6cfb-0215-4e70-bd35-6e327e6fae3d)

## Prerequisites
- Ubuntu 2404LTS
- Docker & Docker Compose
- Git

## Setup Instructions
1. Clone the repository:
```shell
 git clone https://github.com/fujiwat/OE-led-simulation.git
 cd OE-led-simulation
```
2. Build & start the simulation:
```shell
docker compose up --build
```
3. (If you change the program):
```shell
docker compose down
docker compose up -d
``` 
4. Access the Grafana dashboard at: http://localhost:3000 (default login: admin/admin).

## Deployment & Version Control
- All changes and deployments are managed using GitHub. The project follows a branching strategy to ensure stable and incremental updates.
- Repository: GitHub Repository https://github.com/fujiwat/OE-led-simulation

## Future Improvements
- Enable custom time-range selection for graphs (e.g., last 5 minutes or 1 hour).
- Improve Grafana UI design for better insights.

## License
- This project is licensed under the MIT License.

## Author
- DQ4WX0 Fujiwara Takahiro
- BJSLS2 Li Yiran
