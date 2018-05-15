#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

def callback(measurement, dist):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', measurement)
    #dist.publish_closest(measurement.ranges)
    dist.publish(str(closest(measurement.ranges)))

def closest(ranges):
    return min(ranges)

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

    def publish(self, string):
        self.pub.publish(string)

    def closest(self, ranges):
        return min(ranges)

if __name__ == '__main__':
    dist = Distances()
    listener(dist)
