import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
IRpin = 7
GPIO.setup(IRpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
TILTpin = 16
GPIO.setup(TILTpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ir(channel):
    if GPIO.input(IRpin) == GPIO.LOW:
        #print("IR Sensor: Stop!")
    else:
        #print("IR Sensor: Continue.")

def tilt(channel):
    if GPIO.input(TILTpin) == GPIO.LOW:
        #print("Tilt Sensor: Activated.")
    else:
        #print("Tilt Sensor: Stable.")

# LOW when obstacle detected
GPIO.add_event_detect(IRpin, GPIO.BOTH, callback=ir, bouncetime=200) 
# LOW when tilted
GPIO.add_event_detect(TILTpin, GPIO.BOTH, callback=tilt, bouncetime=200)

try:
    while True:
        time.sleep(1) 
except KeyboardInterrupt:
    print("User interrupt.")
finally:
    GPIO.cleanup() 
