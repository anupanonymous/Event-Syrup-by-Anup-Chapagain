from flask import Flask, jsonify, request
from flask_cors import CORS
import temperature_sensor  # Assuming this is your temperature sensor module
import RPi.GPIO as GPIO
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from mfrc522 import SimpleMFRC522

# Initialize Firebase
cred = credentials.Certificate('./serviceAccountKey.json')  # Path to your service account key JSON file
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)
CORS(app)

# Initialize GPIO
RED_PIN = 22
GREEN_PIN = 23
BLUE_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def set_rgb_color(r, g, b):
    GPIO.output(RED_PIN, r)
    GPIO.output(GREEN_PIN, g)
    GPIO.output(BLUE_PIN, b)

@app.route('/temperature', methods=['GET'])
def get_temperature():
    data = temperature_sensor.read_temperature()
    return jsonify(data)

@app.route('/set_color', methods=['POST'])
def set_color():
    data = request.json
    r = data.get('red', 0)
    g = data.get('green', 0)
    b = data.get('blue', 0)
    set_rgb_color(r, g, b)
    return jsonify({'status': 'success', 'red': r, 'green': g, 'blue': b})

# Initialize RFID reader
reader = SimpleMFRC522()

@app.route('/scan_rfid', methods=['GET'])
def scan_rfid():
    try:
        id, text = reader.read()
        print(f"Scanned RFID ID: {id}, Text: {text}")  # Debugging output

        # Return the scanned RFID UID as JSON
        return jsonify({"rfid_uid": str(id)})
    except Exception as e:
        print(f"Error in scan_rfid: {e}")  # Debugging output
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
