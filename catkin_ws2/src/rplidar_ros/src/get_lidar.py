#!/usr/bin/env python
# Software License Agreement (BSD License)

import operator
import os
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def callback(measurement, classes):
    ai = classes[0]
    ai = classes[1]
    if (dist.done):
        dist.done = False
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', measurement)
        #dist.publish_closest(measurement.ranges)
        mini = minimum(measurement.ranges)
        ang = dist.get_angle(measurement.angle_min, measurement.angle_increment, mini[0])
        values = measurement.ranges
        if not str(values[0]) == "inf":
            dist.back = values[0]
        if not str(values[90]) == "inf":
            dist.right = values[90]
        if not str(values[180]) == "inf":
            dist.front = values[180]
        if not str(values[270]) == "inf":
            dist.left = values[270]
        ai.publish(ai.find_move(dist))
        dist.done = True
    else: 
        pass


def closest(values):
    return min(values)

def minimum(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return [min_index, min_value]

def listener(Classes):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('scan', LaserScan, callback, Classes)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

class AI():
    def __init__(self, limit):
        self.pub = rospy.Publisher('moves', String, queue_size=1)
        self.limit = limit

    def find_move(self, dist):
        move = ""
        if dist.front > self.limit:
            move = "forward"
        elif dist.left > self.limit:
            move = "rot_left"
        elif dist.right > self.limit:
            move = "rot_right"
        elif dist.back > self.limit:
            move = "backward"
        else:
            move = "rot_left"
        return move

    def edit_limit(self, limit):
        self.limit = limit

    def publish(self, string):
        self.pub.publish(string)

class Distances():
    def __init__(self):
        self.pub = rospy.Publisher('lidar_data', String, queue_size=1)
        self.closest = 0
        self.done = True
        self.back = 0.0
        self.right = 0.0
        self.front = 0.0
        self.left = 0.0

    def publish(self, string):
        self.pub.publish(string)

    def flip(self, val):
        self.done = val

    def closest(self, ranges):
        return min(ranges)

    def get_angle(self, angle_min, angle_inc, index):
        return angle_min + (angle_inc*index)

    def __str__(self):
        return "Back: " + str(self.back) + os.linesep + "Right: " + str(self.right) + os.linesep + "Front: " + str(self.front) + os.linesep + "Left: " + str(self.left) + os.linesep

if __name__ == '__main__':
    dist = Distances()
    ai = AI(0.20)
    xd = list()
    xd.append(dist)
    xd.append(ai)
    listener(xd)
