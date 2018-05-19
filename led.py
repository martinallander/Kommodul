import RPi.GPIO as GPIO	
import time

def gpio_setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(17, GPIO.OUT)

def LED_on():
	GPIO.output(17, GPIO.HIGH)

def LED_off():
	GPIO.output(17, GPIO.LOW)

def main():
	gpio_setup()
	LED_on()
	time.sleep(1)
	LED_off()

main()
