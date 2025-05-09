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
    """Generate simulated sensor data"""
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(40.0, 70.0)

    # LED auto-adjustment logic
    if temperature > 27 or humidity > 65:
        led_red = random.randint(20, 40)  # Reduce red light proportion
    elif temperature < 23 or humidity < 45:
        led_red = random.randint(60, 80)  # Increase red light proportion
    else:
        led_red = random.randint(45, 55)  # Maintain medium ratio
    
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
    """Send data to InfluxDB"""
    point = Point("simulation_data").tag("sensor", "simulated")
    
    for field, value in data.items():
        point = point.field(field, value)

    write_api.write(bucket=bucket, org=org, record=point)

if __name__ == "__main__":
    while True:
        data = generate_sim_data()
        print("Simulated Data:", data)
        send_data_to_influx(data)
        time.sleep(1)  # Send data every second

class PIDController:
    """Simple PID controller for smooth LED lighting adjustments"""
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, current_value):
        """Compute adjustment value"""
        error = setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative

# Initialize PID controllers
red_pid = PIDController(0.5, 0.1, 0.05)
blue_pid = PIDController(0.4, 0.08, 0.04)

def adjust_led_lighting(sensor_data):
    """Adjust LED lighting using PID controllers"""
    temp = sensor_data["temperature"]
    humidity = sensor_data["humidity"]
    
    # Set target lighting values
    target_red = 60 if temp < 25 else 40
    target_blue = 100 - target_red
    
    # Compute adjustment values using PID
    led_red = int(red_pid.compute(target_red, temp))
    led_blue = int(blue_pid.compute(target_blue, humidity))

    # Limit lighting range
    led_red = max(20, min(80, led_red))
    led_blue = 100 - led_red

    crop_growth = (led_red * 0.3 + led_blue * 0.7) / 100
    return {"led_red": led_red, "led_blue": led_blue, "crop_growth": round(crop_growth, 2)}

