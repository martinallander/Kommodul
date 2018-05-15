#!/usr/bin/env python
# Software License Agreement (BSD License)

import operator
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def callback(measurement, dist):
    if (dist.done):
        dist.flip(False)
        rospy.loginfo(rospy.get_caller_id() + 'I heard %s', measurement)
        #dist.publish_closest(measurement.ranges)
        mini = minimum(measurement.ranges)
        ang = dist.get_angle(measurement.angle_min, measurement.angle_increment, mini[0])
        dist.publish(str(ang))
        dist.flip(True)
    else: 
        pass


def closest(values):
    return min(values)

def minimum(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return [min_index, min_value]

def listener(Distances):

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('scan', LaserScan, callback, Distances)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

class Distances():
    def __init__(self):
        self.pub = rospy.Publisher('moves', String, queue_size=1)
        self.closest = 0
        self.done = True

    def publish(self, string):
        self.pub.publish(string)

    def flip(self, val):
        self.done = val

    def closest(self, ranges):
        return min(ranges)

    def get_angle(self, angle_min, angle_inc, index):
        return angle_min + (angle_inc*index)

if __name__ == '__main__':
    dist = Distances()
    listener(dist)
