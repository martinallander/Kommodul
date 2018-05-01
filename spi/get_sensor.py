import spidev
import time
import struct
import RPi.GPIO as GPIO
#import keyboard

def init_sens_modul():
        sensmodul_spi = spidev.SpiDev()
        sensmodul_spi.open(0, 0)
        sensmodul_spi.max_speed_hz = 10000
        return sensmodul_spi
    
def init_styr_modul():
        styrmodul_spi = spidev.SpiDev()
        styrmodul_spi.open(0, 1)
        styrmodul_spi.max_speed_hz = 10000
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


#define DATA_ERROR 0x10

def request_ALL(spi_buss):
        spi_buss.writebytes([0x01])
        
def request_ACC(spi_buss):
        spi_buss.writebytes([0x02])

def request_GYRO(spi_buss):
        spi_buss.writebytes([0x03])

def request_DIST(spi_buss):
        spi_buss.writebytes([0x04])

def request_IR(spi_buss):
        spi_buss.writebytes([0x05])


def check_ACK(spi_buss):
        #while True:
                ack = spi_buss.readbytes(1)
                #print(ack)
                ###
                if ack[0] == 0x11:
                        return True
                else:
                        return False

def read_data(spi_buss, length, ls):
        i = 0
        while i < length:
                ls.append(spi_buss.readbytes(1)[0])
                i += 1
        return ls

                        
def main():
        gpio_setup()
        sensmodul = init_sens_modul()
        set_mode(sensmodul, 0b00)
        shit = list()
        while True:
                shit[:] = []
                request_GYRO(sensmodul)
        #for i in range(0,14):
         #       print(sensmodul.readbytes(1))
        #request_ALL(sensmodul)
                if (check_ACK(sensmodul)):
                        print(read_data(sensmodul, 12, shit))
        sensmodul.close()

main()
