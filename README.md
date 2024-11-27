
# Project: Educational Kafka System for Weather Data Processing

## Description
This project serves as an educational example of using Apache Kafka for real-time data transmission and processing. It includes three main components:

1. **Producer**: Generates and sends weather data to Kafka.
2. **Processor**: Processes data, detects anomalies, and publishes results to another Kafka topic.
3. **Notification**: Subscribes to processed data and sends alerts in case of detected anomalies.

The project demonstrates the basics of working with Kafka, including creating producers, processors, and consumers. It is ideal for learning the fundamentals of stream data processing.

---

## Project Contents
- **`docker-compose.yml`**: Describes all services, including Kafka, Zookeeper, and the application.
- **Component folders**:
  - `producer`: Code for generating and sending data.
  - `processor`: Code for processing data and detecting anomalies.
  - `notification`: Code for alerting about anomalies.

---

## How to Run the Project

### Requirements
- Docker and Docker Compose installed on your system.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone <repo-URL>
   cd <project_folder>
   ```
2. Start the containers:
   ```bash
   docker compose up --build
   ```
3. Verify that all services are running. Logs from `producer`, `processor`, and `notification` should appear in the terminal.

### Steps to Stop
To stop all containers:
```bash
docker compose down
```

---

## Key Points to Consider

1. **Kafka Topics**:
   - Ensure the `weather-processed` topic is automatically created. If it is not, create it manually:
     ```bash
     docker exec -it <kafka-container> kafka-topics --bootstrap-server localhost:9092 --create --topic weather-processed --partitions 1 --replication-factor 1
     ```

2. **Docker Network**:
   - All services use a shared `kafka-network`. Verify that all services can communicate with each other.

3. **Logs**:
   - If the `notification` service is not processing messages, check the logs for Kafka, `processor`, and `notification` for errors.

4. **Debugging**:
   - Utilize the debug logs added in each service to identify issues.

---

## Potential Improvements
- Add Grafana and Prometheus for monitoring the Kafka setup.
- Implement automated tests to ensure correct message processing.
- Extend support for handling multiple Kafka topics or advanced scenarios.
