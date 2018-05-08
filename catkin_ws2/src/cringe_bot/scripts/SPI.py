import spidev
import time
import struct
import binascii
from Sensor_Data import Sensor_Data

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
                self.done = True
                self.move_ready = True
                self.sd = Sensor_Data()
                
        def set_modes(self, module, mode_id):
        	module.mode = mode_id

        def request_sensor(self, sensor):
                if sensor.lower() == "all":
                        self.read("acc")
                        self.read("angle")
                        self.read("dist")
                        self.read("ir")
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

        def check_ACK(self):
                ack = self.sens.readbytes(1)[0]
                #print(ack)
                if (ack == 0x11):
                        return True
                else:
                        return False

        def bytes_to_float(self, four_bytes):
                b_ascii = binascii.hexlify(bytearray(four_bytes))
                f = struct.unpack('f', b_ascii.decode("hex") )[0]
                return f
                
        def read_sensor(self):
                sensor_data = list()
                four_bytes = list()
                i = 1
                while i <= self.length:
                        four_bytes.append(self.sens.readbytes(1)[0])
                        if i % 4 == 0:
                                sensor_data.append(self.bytes_to_float(four_bytes))
                                four_bytes[:] = []
                        i += 1
                self.length = 0
                return sensor_data

        def read(self, sensor):
                self.done = False
                if sensor.lower() == "all":
                        self.request_sensor("all")
                elif sensor.lower() == "acc":
                        self.request_sensor("acc")
                        if self.check_ACK():
                                self.sd.set_acc(self.read_sensor())
                                self.done = True
                        else:
                                self.done = True
                elif sensor.lower() == "angle":
                        self.request_sensor("angle")
                        if self.check_ACK():
                                self.sd.set_angle(self.read_sensor())
                                self.done = True
                        else:
                                self.done = True
                elif sensor.lower() == "dist":
                        self.request_sensor("dist")
                        if self.check_ACK():
                                self.sd.set_dist(self.read_sensor())
                                self.done = True
                        else:
                                self.done = True
                elif sensor.lower() == "ir":
                        self.request_sensor("ir")
                        if self.check_ACK():
                                self.sd.set_ir(self.read_sensor())
                                self.done = True
                        else:
                                self.done = True
                else:
                        self.length = 0
                        print("unknown request")

                

        def move(self, command):
                self.done = False
                if command == "forward":
			self.styr.writebytes([0x01])
                elif command == "backward":
                        self.styr.writebytes([0x02])
                elif command == "rotleft":
                        self.styr.writebytes([0x03])
                elif command == "rotright":
                        self.styr.writebytes([0x04])
		elif command == "turnleft":
                        self.styr.writebytes([0x05])
		elif command == "turnright":
                        self.styr.writebytes([0x06])
                self.check_move_ready()
                self.done = True
                return self.move_ready

        def check_move_ready(self):
                #i = 0
                #while i < 10:
                ready = self.styr.readbytes(1)[0]
                #print("Ready status:")
                #print(ready)
                #        i +=1
                if ready == 0xD0:
                        self.move_ready = False
                else:
                        self.move_ready = True
