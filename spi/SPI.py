import spidev
import time
import struct
import RPi.GPIO as GPIO
import binascii

def gpio_setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)

class SPI:
        def __init__(self, clk_speed):
                self.sens = spidev.SpiDev()
                self.sens.open(0, 0)
                self.sens.max_speed_hz = clk_speed
                self.styr = spidev.SpiDev()
                self.styr.open(0, 1)
                self.styr.max_speed_hz = clk_speed
                self.sens.mode =  0b00
                self.styr.mode =  0b00
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
                        print("xD")

        def check_ACK(self):
                ack = self.sens.readbytes(1)[0]
                #print(ack)
                if (ack == 0x11):
                        return True
                else:
                        return False

        def bytes_to_float(self, four_bytes):
                print(four_bytes)
                #four_bytes = four_bytes[::-1]
               # print(four_bytes)
                b_ascii = binascii.hexlify(bytearray(four_bytes))
                #print(b_ascii)
                f = struct.unpack('f', b_ascii.decode('hex') )[0]
                print(f)
                
        def read_sensor(self):
                four_bytes = list()
                i = 1
                while i <= self.length:
                        four_bytes.append(self.sens.readbytes(1)[0])
                        if i % 4 == 0:
                                self.bytes_to_float(four_bytes)
                                four_bytes[:] = []
                        i += 1
                self.length = 0

        def read(self, sensor):
                self.request_sensor(sensor)
                if self.check_ACK():
                        self.read_sensor()

def main():
        gpio_setup()
        sp = SPI(10000)
        #four_bytes = list()
        while True:
                #sp.request_sensor("angle")
                print("New angle:")
                sp.read("angle")
                #sp.read_sensor()
                time.sleep(5)
        sp.sens.close()
        sp.styr.close()
        
main()
