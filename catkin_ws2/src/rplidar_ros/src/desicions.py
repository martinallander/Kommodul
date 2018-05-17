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
    ai.publish(str(lidar.forward))
    for i in range(90 + self.angle, 180 + self.angle):
        ai.publish(str(lidar.minimum[i]))
#    ai.publish(str(lidar.backward))


def callback_dist(irdata, ai):
    ai.publish(str(irdata.ir_right))

def closest(values):
    return min(values)


def minimum(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return [min_index, min_value]

def listener(AI):

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('lidar_data', Lidardistances, callback, AI)
    rospy.Subscriber('distressed', IRdata, callback_dist, AI)
    rospy.spin()

class AI():
    def __init__(self):
        self.pub = rospy.Publisher('moves', String, queue_size=1)
        self.found = False
        self.forward = False
        self.right = False
        self.ir_forward = [0] * 64
        self.ir_right = [0] * 64
        self.lidar = ""

    def publish(self, string):
        self.pub.publish(string)



if __name__ == '__main__':
    ai = AI()
    listener(ai)

