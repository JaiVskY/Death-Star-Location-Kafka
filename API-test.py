import requests
import json
import time

# Example API response:
# {
#   "iss_position": {
#     "longitude": "-156.6092",
#     "latitude": "-33.4760"
#   },
#   "message": "success",
#   "timestamp": 1774552449
# }


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
        print(f"Error fetching data from API: {e}")
        return None

iss_data = fetch_iss_location()

print(iss_data)
