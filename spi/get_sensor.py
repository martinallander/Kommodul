import spidev
import time
import struct
import RPi.GPIO as GPIO
#import keyboard

sensmodul_spi = spidev.SpiDev()
sensmodul_spi.open(0, 0)
sensmodul_spi.max_speed_hz = 2000000
    

styrmodul_spi = spidev.SpiDev()
styrmodul_spi.open(0, 1)
styrmodul_spi.max_speed_hz = 2000000

print('Please wait.. \n .... \n ......... \n')

#def format_sensor_data():

def gpio_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)

def set_mode(module, mode_id):
    module.mode = mode_id

def write_sensmodul(input):
    msb = input >> 8
    lsb = input & 0xFF
    sensmodul_spi.xfer([msb, lsb])
    
def read_byte():
	resp = sensmodul_spi.readbytes(1)
	return resp[0]

def unpack_bytes(bytes):
	return struct.unpack("f", bytes)

def main():
	#sensmodul_spi.writebytes([0xAA]) #Start SPI
	struct.pack('f', 3.141592654)
	print(struct.unpack('f', b'\xdb\x0fI@'))

main()
