from confluent_kafka import Producer
import json
import time
import random

producer = Producer({'bootstrap.servers': 'kafka:9092'})

cities = ['Moscow', 'New York', 'London', 'Tokyo']

def produce_weather_data():
    while True:
        city = random.choice(cities)
        data = {
            "city": city,
            "temperature": random.randint(-30, 40),
            "humidity": random.randint(10, 90),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S")
        }
        producer.produce('weather-data', key=city, value=json.dumps(data))
        print(f"Produced: {data}")
        producer.flush()
        time.sleep(1)

if __name__ == "__main__":
    produce_weather_data()
