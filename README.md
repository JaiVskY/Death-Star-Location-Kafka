# 🛰️ ISS Real-Time Data Streaming Pipeline

An end-to-end data engineering project that tracks the International Space Station (ISS). This pipeline demonstrates real-time data ingestion, stream processing with **Apache Kafka**, and live geospatial visualization.

---

## 🏗️ Architecture Overview

The project follows a decoupled "Producer-Consumer" architecture:
1. **Producer**: A Python script that polls the Open Notify API every 5 seconds.
2. **Broker**: **Apache Kafka (KRaft mode)** running in a Docker container.
3. **Consumer (Analytics)**: Processes coordinates to calculate real-time speed (km/h) and total distance.
4. **Visualizer**: A **Streamlit** dashboard that renders the ISS position on a live map.

---

## 🛠️ Infrastructure Management (Docker & Kafka)

The following commands manage the lifecycle of your Kafka broker.

### 1. Start the Environment
Launch the Kafka broker in "Detached" mode.
```powershell
docker-compose up -d# 🛰️ ISS Real-Time Data Streaming Pipeline

An end-to-end data engineering project that tracks the International Space Station (ISS). This pipeline demonstrates real-time data ingestion, stream processing with **Apache Kafka**, and live geospatial visualization.

---

## 🏗️ Architecture Overview

The project follows a decoupled "Producer-Consumer" architecture:
1. **Producer**: A Python script that polls the Open Notify API every 5 seconds.
2. **Broker**: **Apache Kafka (KRaft mode)** running in a Docker container.
3. **Consumer (Analytics)**: Processes coordinates to calculate real-time speed (km/h) and total distance.
4. **Visualizer**: A **Streamlit** dashboard that renders the ISS position on a live map.

---

## 🛠️ Infrastructure Management (Docker & Kafka)

The following commands manage the lifecycle of your Kafka broker.

### 1. Start the Environment
Launch the Kafka broker in "Detached" mode.
```powershell
docker-compose up -d


docker exec -it kafka /usr/bin/kafka-topics --create --topic iss-tracking --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


py -m streamlit run Visualise.py