#!/usr/bin/env python
# Software License Agreement (BSD License)

import operator
import os
import rospy
from std_msgs.msg import String
from cringe_bot.msg import IRdata
from cringe_bot.msg import Lidardistances
import ast

def callback(lidar, ai):
    ai.get_lidar(lidar)
    #ai.publish(str(lidar.angle))
   # for i in range(90 + lidar.angle, 270 - lidar.angle):
   #     if lidar.minimum[i] == 0:
   #         ai.publish(str(i))
#    ai.publish(str(lidar.backward))



def callback_dist(irdata, ai):
    ai.get_distressed(irdata)

def closest(values):
    return min(values)


def mini_range(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return [min_index, min_value]

def listener(AI):

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('lidar_data', Lidardistances, callback, AI)
    rospy.Subscriber('distressed', IRdata, callback_dist, AI)
    rospy.spin()

class AI():
    def __init__(self):
        self.pub = rospy.Publisher('spi_commands', String, queue_size=1)
        self.forward = False
        self.right = False
        self.left = False
        self.right = False
        self.found = False
        self.allowed = [0] * 64
        self.has_forward = False
        self.has_right = False
        self.ir_forward = [0] * 64
        self.ir_right = [0] * 64

    def publish(self, string):
        self.pub.publish(string)

    def decide(self):
        if forward:
            self.publish("forward")
        else:
            self.publish("rot_right")

    def get_lidar(self,lidar):
        self.forward = lidar.forward
        self.backward = lidar.backward
        self.right = lidar.right
        self.left = lidar.left
        self.allowed = lidar.allowed

    def get_distressed(self,irdata):
        self.found = irdata.found
        self.has_forward = irdata.has_forward
        self.ir_forward = irdata.ir_forward
        self.has_right = irdata.has_right
        self.ir_right = irdata.ir_right


if __name__ == '__main__':
    ai = AI()
    listener(ai)

