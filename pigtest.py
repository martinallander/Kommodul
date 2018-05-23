import time
import os

#time.sleep(1)

#os.system("sudo pigpiod")

#time.sleep(1)

#os.system("olovmonkas")

time.sleep(1)

import pigpio

pi = pigpio.pi()
pi.set_mode(4, pigpio.INPUT)
pi.set_mode(17, pigpio.OUTPUT)

def auto_led():	
	prev_input = 0
	while True:
		input = pi.read(4)
		#if ((not prev_input) and input):
		#	print("switch on")
		#prev_input = input
		print(pi.read(4))
		time.sleep(1)

def falling_led():
	while True:
		if pi.wait_for_edge(4, pigpio.FALLING_EDGE, 5.0):
			pi.write(17, 1)
			print("button pressed")
			time.sleep(1)
			pi.write(17, 0)
		time.sleep(0.05)

def led_test():
	while True:
		pi.write(17, 1)
		print(pi.read(17))
		time.sleep(1)
		pi.write(17, 0)
		time.sleep(1)
		print(pi.read(17))

def run():
	try:
		auto_led()
	except KeyboardInterrupt:
		pi.write(17,0)
		pi.stop()
		print("done")

run()
