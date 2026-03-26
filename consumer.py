import json
from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'iss-watchers',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
consumer.subscribe(['iss-tracking'])

print("Waiting for ISS location ..")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        # Decode the JSON data
        data = json.loads(msg.value().decode('utf-8'))
        lat = data['latitude']
        lon = data['longitude']
        
        print(f" ISS Spotted at | Lat: {lat} | Lon: {lon} | Time: {data['timestamp']}")

except KeyboardInterrupt:
    print("Closing tracker...")
finally:
    consumer.close()