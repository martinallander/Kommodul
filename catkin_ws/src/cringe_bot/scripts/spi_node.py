#!/usr/bin/env python
# Software License Agreement (BSD License)

from SPI import SPI
import rospy
from std_msgs.msg import String

move_commands = ["rotright", "rotleft", "forward", "backward"]
#global spi = SPI(10000)

def callback(data, spi_node):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    print(data.data)
    if data.data.lower() in move_commands:
        spi_node.insert_styr_back(data.data.lower())
    else:
        spi_node.insert_sens_back(data.data.lower())
    print(data.data)
    spi_node.perform_action()

def listener(spi_node):
    rospy.init_node('spi_node', anonymous=True)
    pub = rospy.Publisher('sensor_data', String, queue_size=100)
    rospy.Subscriber('spi_commands', String, callback, spi_node)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
    spi_node.close()

class SPI_node:
    def __init__(self):
        self.spi = SPI(10000)
        self.next = ""
        self.next_type = False
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
                print(self.spi.move(self.styr_queue.pop(0)))
            else:
                print(self.spi.read(self.sens_queue.pop(0)))
        else:
            return None

    def close(self):
        self.spi.sens.close()
        self.spi.styr.close()

if __name__ == '__main__':
    sp = SPI_node()
    listener(sp)
