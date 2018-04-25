import spidev
import time
import struct
import RPi.GPIO as GPIO
#import keyboard

def init_sens_modul():
        sensmodul_spi = spidev.SpiDev()
        sensmodul_spi.open(0, 0)
        sensmodul_spi.max_speed_hz = 2000000
        return sensmodul_spi
    
def init_styr_modul():
        styrmodul_spi = spidev.SpiDev()
        styrmodul_spi.open(0, 1)
        styrmodul_spi.max_speed_hz = 2000000
        return styrmodul_spi

print('Please wait.. \n .... \n ......... \n')

#def format_sensor_data():

def gpio_setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)

def set_mode(module, mode_id):
        module.mode = mode_id
    
def read_byte(spi_buss):
        resp = spi_buss.readbytes(1)
        return resp[0]

def unpack_bytes(bytes):
        return struct.unpack('f', bytes)

def read_sensor_init(spi_buss):
        start = read_byte(spi_buss)
        if start == 0x00:
                length = read_byte(spi_buss)
                return length
        return 0

def request_ACC(spi_buss):
        spi_buss.writebytes([0x01])

def request_GYRO(spi_buss):
        spi_buss.writebytes([0x02])

def request_IR(spi_buss):
        spi_buss.writebytes([0x03])

def request_DIST(spi_buss):
        spi_buss.writebytes([0x04])

def request_ALL(spi_buss):
        spi_buss.writebytes([0x05])

def check_ACK(spi_buss):
        #while True:
                ack = spi_buss.readbytes(1)[0]
                print(ack)
                if ack == 0x11:
                        return True
                else:
                        return False

def read_data(spi_buss, length):
        i = 0
        while i < length:
                print(spi_buss.readbytes(1)[0])
                i += 1
    
def main():
        gpio_setup()
        sensmodul = init_sens_modul()
        set_mode(sensmodul, 0b00)
        request_IR(sensmodul)
       # request_IR(sensmodul)
        if (check_ACK(sensmodul)):
                length = spi_buss.readbytes(1)[0]
                read_data(sensmodul, length)
        sensmodul.close()

main()
