from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import random
import time

# InfluxDB 2.x connection settings
url = "http://influxdb:8086"
token = "my-super-secret-token"
org = "my-org"
bucket = "simulation_db"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

def generate_sim_data():
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(40.0, 70.0)
    led_red = random.randint(0, 100)
    led_blue = 100 - led_red
    crop_growth = (led_red * 0.3 + led_blue * 0.7) / 100
    return {
        "temperature": round(temperature, 2),
        "humidity": round(humidity, 2),
        "led_red": led_red,
        "led_blue": led_blue,
        "crop_growth": round(crop_growth, 2)
    }
    
def send_data_to_influx(data):
    # Create a Point object with measurement "simulation_data" and a tag "sensor=simulated"
    point = Point("simulation_data").tag("sensor", "simulated")
    # Set simulation data fields
    for field, value in data.items():
        point = point.field(field, value)
    # Execute write operation (specifying bucket, org, and record)
    write_api.write(bucket=bucket, org=org, record=point)

if __name__ == "__main__":
    while True:
        data = generate_sim_data()
        print("Simulated Data:", data)
        send_data_to_influx(data)
        time.sleep(1)  # Send data every second

