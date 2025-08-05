import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def read_rfid():
    try:
        id, text = reader.read()
        return {'id': id, 'text': text}
    finally:
        GPIO.cleanup()
