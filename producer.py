import requests
import json
import time
from confluent_kafka import Producer

# Kafka Configuration
conf = {'bootstrap.servers': 'localhost:9092'}   #address of the container => PC
producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Location Sent to {msg.topic()} [{msg.partition()}]")

def fetch_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        return {
            "timestamp": data['timestamp'],
            "latitude": data['iss_position']['latitude'],
            "longitude": data['iss_position']['longitude']
        }
    except Exception as e:
        print(f"Error fetching API: {e}")
        return None

print("Starting ISS Producer... Press Ctrl+C to stop (keyboard interrupt).")

try:
    while True:
        iss_data = fetch_iss_location()  #Gets the fresh coordinates.
        print(iss_data) #Prints the coordinates in the terminal.
        if iss_data:
            # Send data as a JSON string
            producer.produce(
                'iss-tracking', 
                value=json.dumps(iss_data), 
                callback=delivery_report
            )
            producer.flush() # Ensure it sends immediately
        
        time.sleep(5) # Wait 5 seconds before next update
except KeyboardInterrupt:
    print("Stopping Producer...")