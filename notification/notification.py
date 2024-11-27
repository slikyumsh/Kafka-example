from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'notification-service',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': False
})

consumer.subscribe(['weather-processed'])

def notify():
    print("Notification service started. Waiting for messages...")
    while True:
        try:
            msg = consumer.poll(1.0)
            if msg is None:
                print("No message received, waiting...")
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            print(f"Raw message: {msg.value()}")
            data = json.loads(msg.value().decode('utf-8'))
            print(f"Processed data: {data}")

            if data.get('anomaly'):
                print(f"[ALERT] {data['message']} in {data['city']}!")

        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    notify()
