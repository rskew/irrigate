import RPi.GPIO as GPIO
import time
import schedule

GPIO.setmode(GPIO.BCM)

solenoid_1_pin = 2
solenoid_2_pin = 3

GPIO.setup(solenoid_1_pin, GPIO.OUT)
GPIO.setup(solenoid_2_pin, GPIO.OUT)
# pins are active low so initialise high
GPIO.output(solenoid_1_pin, True)
GPIO.output(solenoid_2_pin, True)

def irrigation_start():
    print 'Starting irrigation at:', time.localtime()
    GPIO.output(solenoid_1_pin, False)

def irrigation_stop():
    print 'Stopping irrigation at:', time.localtime()
    GPIO.output(solenoid_1_pin, True)


schedule.every().day.at("18:40").do(irrigation_start)
schedule.every().day.at("18:41").do(irrigation_stop)


while True:
    schedule.run_pending()
    time.sleep(1)
