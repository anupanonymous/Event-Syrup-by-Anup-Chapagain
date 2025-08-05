import adafruit_dht
import board
import time

# Initialize the DHT device, with data pin connected to GPIO4
dht_device = adafruit_dht.DHT11(board.D4)

def read_temperature():
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        # Return values as integers to avoid issues with decimal points
        return {'temperature': int(temperature_c), 'humidity': int(humidity)}
    except RuntimeError as error:
        return {'error': str(error)}

if __name__ == "__main__":
    while True:
        result = read_temperature()
        print(result)
        time.sleep(2)
