# OpenSpeedMonitor
A lightweight tool to monitor network speed and latency.

## Features
- Automatically test download/upload speed
- Save results to SQLite database
- Web dashboard with Chart.js

## How to Use
```bash
# 本地运行
pip install -r requirements.txt
python app.py

# Docker运行
docker build -t openspeedmonitor .
docker run -p 5000:5000 openspeedmonitor
