import streamlit as st
import pandas as pd
import json
from confluent_kafka import Consumer
import time

st.set_page_config(page_title="ISS Tracker", layout="wide")
st.title("🛰️ ISS Real-Time Path Tracker")

# 1. Setup Kafka with a fresh Group ID to ensure we get data immediately
@st.cache_resource
def get_kafka_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': f'group_{int(time.time())}', # Unique ID every time you restart
        'auto.offset.reset': 'latest'
    })

consumer = get_kafka_consumer()
consumer.subscribe(['iss-tracking'])

# 2. Session State to store the breadcrumbs (the path)
if 'path_history' not in st.session_state:
    st.session_state.path_history = []

placeholder = st.empty()

# 3. The Main Loop
while True:
    # Check Kafka for new coordinates (wait max 1 second)
    msg = consumer.poll(1.0)
    
    if msg is not None and not msg.error():
        # Received data from Producer
        data = json.loads(msg.value().decode('utf-8'))
        
        new_coord = {
            'lat': float(data['latitude']), 
            'lon': float(data['longitude'])
        }
        
        # Add to history
        st.session_state.path_history.append(new_coord)
        
        # Keep only the last 200 points (about 15-20 minutes of flight)
        if len(st.session_state.path_history) > 200:
            st.session_state.path_history.pop(0)

    # 4. Update the UI if we have data
    if st.session_state.path_history:
        df = pd.DataFrame(st.session_state.path_history)
        current = st.session_state.path_history[-1]

        with placeholder.container():
            # Big beautiful metrics at the top
            col1, col2, col3 = st.columns(3)
            col1.metric("Latitude", f"{current['lat']:.4f}")
            col2.metric("Longitude", f"{current['lon']:.4f}")
            col3.metric("Path Points", len(df))

            # The Map (Using the stable built-in version)
            # This will show the current position as a big dot and the history as smaller dots
            st.map(df, size=20, color='#ffff00') 
            
            st.caption("🟡 Yellow dots represent the path traced in the last few minutes.")
    else:
        placeholder.info("📡 Waiting for Kafka stream... ensure your producer is running!")

    time.sleep(0.1) # Prevent CPU from hitting 100%