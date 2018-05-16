#!/usr/bin/env python
# Software License Agreement (BSD License)

import operator
import os
import rospy
from std_msgs.msg import String
import ast

def callback(array, ai):
    values = ast.literal_eval(array)
    ai.publish(str(values[0]))


def callback_dist(ir, ai):
    ai.publish(ir)

def closest(values):
    return min(values)


def minimum(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return [min_index, min_value]

def listener(AI):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('lidar_data', String, callback, AI)
    rospy.Subscriber('distressed', String, callback_dist, AI)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

class AI():
    def __init__(self):
        self.pub = rospy.Publisher('moves', String, queue_size=1)

    def publish(self, string):
        self.pub.publish(string)

if __name__ == '__main__':
    ai = AI()
    listener(ai)
