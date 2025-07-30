import os
import json
from dotenv import load_dotenv
from azure.eventhub import EventHubProducerClient, EventData

load_dotenv()

conn_str = os.getenv("EVENT_HUB_CONN_STRING")
eventhub_name = "taxi-trips"

producer = EventHubProducerClient.from_connection_string(
    conn_str=conn_str, eventhub_name=eventhub_name
)

event_data_batch = producer.create_batch()
trip_data = {
    "ContentData": {
        "vendorID": "V123",
        "tripDistance": 0.5,
        "passengerCount": 5,
        "paymentType": "2"
    }
}
event_data_batch.add(EventData(json.dumps(trip_data)))
producer.send_batch(event_data_batch)
producer.close()
