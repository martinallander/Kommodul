#!/usr/bin/env python
# Software License Agreement (BSD License)

from SPI import SPI
import rospy
import time
from std_msgs.msg import String
from cringe_bot.msg import Sensordata

move_commands = ["rotright", "rotleft", "forward", "backward", "turnleft", "turnright"]
#global spi = SPI(10000)

def callback(data, spi_node):
    if data.data.lower() in move_commands:
        spi_node.insert_styr_back(data.data.lower())
	spi_node.perform_action()
    #else:
        #spi_node.insert_sens_back(data.data.lower())
    

def listener(spi_node):
    rospy.init_node('spi_node', anonymous=True)
    pub = rospy.Publisher('sensor', Sensordata, queue_size=1)
    rospy.Subscriber('spi_commands', String, callback, spi_node)
    # spin() simply keeps python from exiting until this node is stopped
    rate = rospy.Rate(12) # 30hz
    i = 0
    rate.sleep()
    while not rospy.is_shutdown():
	spi_node.perform_action()
        sd = Sensordata(spi_node.spi.sd.acc, spi_node.spi.sd.angle, spi_node.spi.sd.ir, spi_node.spi.sd.tof)
        #rospy.loginfo(sd)
        pub.publish(sd)
        rate.sleep()
    rospy.spin()
    spi_node.close()

class SPI_node:
    def __init__(self):
        self.spi = SPI(150000)
        self.styr_queue = list()
        self.sens_queue = list()

    def insert_sens_back(self, data):
        self.sens_queue.append(data)

    def insert_sens_front(self, data):
        self.sens_queue = [data.data] + spi_node.sens_queue

    def insert_styr_back(self, data):
        self.styr_queue.append(data)

    def insert_styr_front(self, data):
        self.styr_queue = [data.data] + spi_node.sens_queue

    def perform_action(self):
        if(self.spi.done == True):
            if not len(self.styr_queue) == 0:  
                if  self.spi.move(self.styr_queue[0]):
                    self.styr_queue.pop(0)
                else:
                     self.spi.read(self.sens_queue.pop(0))
            else:
                self.spi.read("acc")
		self.spi.read("angle")
		self.spi.read("dist")
                self.spi.read("ir")
        else:
            return None

    def close(self):
        self.spi.sens.close()
        self.spi.styr.close()

if __name__ == '__main__': 
    print("Starting!")
    sp = SPI_node()
    listener(sp)
