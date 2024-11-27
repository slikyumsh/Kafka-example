from confluent_kafka import Consumer, Producer
import json

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'weather-processor',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe(['weather-data'])

producer = Producer({'bootstrap.servers': 'kafka:9092'})

def process_weather_data():
    while True:
        msg = consumer.poll(1.0)
        if msg is None: continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        data = json.loads(msg.value().decode('utf-8'))
        anomaly = data['temperature'] < -10 or data['temperature'] > 35
        processed_data = {
            **data,
            "anomaly": anomaly,
            "message": "Anomaly detected!" if anomaly else "Weather normal"
        }
        producer.produce('weather-processed', key=data['city'], value=json.dumps(processed_data))
        print(f"Processed: {processed_data}")
        producer.flush()

if __name__ == "__main__":
    process_weather_data()
