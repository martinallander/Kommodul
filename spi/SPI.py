import spidev
import time
import struct
import RPi.GPIO as GPIO


def gpio_setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)

class SPI:
        def __init__(self, clk_speed):
	gpio_setup()
                self.sens = spidev.SpiDev()
                self.sens.open(0, 0)
                self.sens.max_speed_hz = clk_speed
	self.styr = spidev.SpiDev()
                self.styr.open(0, 1)
                self.styr.max_speed_hz = clk_speed
	set_mode(self.sens, 0b00)
	set_mode(self.styr, 0b00)
                self.length = 0

                

	def set_modes(self, module, mode_id):
        	module.mode = mode_id

        def request_sensor(self, sensor):
                if sensor.lower() == "all":
                        pass
                elif sensor.lower() == "acc":
                        self.length = 12
                        self.sens.writebytes([0x02])
                elif sensor.lower() == "angle":
                        self.length = 12
                        self.sens.writebytes([0x03])
                elif sensor.lower() == "dist":
                        self.length = 4
                        self.sens.writebytes([0x04])
                elif sensor.lower() == "ir":
                        self.length = 256
                        self.sens.writebytes([0x05])
                else:
                        self.length = 0

        def check_ACK(self):
                ack = sens.readbytes(1)[0]
                if (ack == 0x11):
                        return True
                else:
                        return False

        def bytes_to_float(self, four_bytes):
                

        def read_sensor(self):
                four_bytes = list()
                i = 1
                while i <= self.length:
                        four_bytes.append(spi_buss.readbytes(1)[0])
                        if i % 4 == 0:
                                
                        
