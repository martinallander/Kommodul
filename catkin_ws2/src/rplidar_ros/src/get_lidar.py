#!/usr/bin/env python
# Software License Agreement (BSD License)

import operator
import os
import rospy
import math
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from cringe_bot.msg import Lidardistances

MIN_VALUE = 0.3
LEG_LENGTH = 0.15
ANGLE_DRIFT = 10

def callbackward(measurement, classes):
    dist = classes[0]
    if (dist.done):
        dist.done = False
        #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', measurement)
        #dist.publish_closest(measurement.ranges)
        #mini = minimum(measurement.ranges)
        #ang = dist.get_angle(measurement.angle_min, measurement.angle_increment, mini[0])
        #if min_value < 0.3:
        values = measurement.ranges
        dist.set_all(values)
        dist.check_moves()
        dist.publish()
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

    rospy.Subscriber('scan', LaserScan, callbackward, Classes)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

class Distances():
    def __init__(self, limit):
        self.pub = rospy.Publisher('lidar_data', Lidardistances, queue_size=1)
        self.limit = limit
        self.done = True
        self.backward = True
        self.right = True
        self.forward = True
        self.left = True
        self.turn_right = True
        self.turn_left = True
        self.all = [0.0] * 360
        self.allowed = [1] * 360
        self.angle = int(math.degrees(math.acos(LEG_LENGTH/self.limit)))

    def check_moves(self):
        self.backward = True
        self.right = True
        self.forward = True
        self.left = True
        self.turn_right = True
        self.turn_left = True
        for i in range(90 - ANGLE_DRIFT + self.angle, 270 + ANGLE_DRIFT - self.angle):
            if self.allowed[i] == 0:
                if i < 90  + self.angle:
                    self.turn_right = False
                    break
                elif i > 270  - self.angle:
                    self.turn_left = False
                    break
                else:
                    if i > 90 + ANGLE_DRIFT + self.angle:
                        self.forward = False
                        self.turn_left = False
                        self.turn_right = False
                    else:
                        self.forward = False
                        self.turn_right = False
                    if i > 270 - ANGLE_DRIFT + self.angle:
                        self.forward = False
                        self.turn_left = False
                    else:
                        self.forward = False
                        self.turn_left = False
                        self.turn_right = False
                    break

        for i in range(270 + self.angle, 360):
            if self.allowed[i] == 0:
                self.backward = False
                break

        for i in range(0, 90 - self.angle):
            if self.allowed[i] == 0:
                self.backward = False
                break

        for i in range(70, 110):
            if self.allowed[i] == 0:
                self.right = False
                break

        for i in range(250, 290):
            if self.allowed[i] == 0:
                self.left = False
                break


    def set_all(self, values):
        i = 0
        for val in values:
            if not str(val) == "inf":
                self.all[i] = val
                if self.all[i] < self.limit:
                    self.allowed[i] = 0
                else:
                    self.allowed[i] = 1
            i += 1

    def publish(self):
        ld = Lidardistances(self.forward, self.backward, self.right, self.left, self.turn_right, self.turn_left, self.allowed, self.limit, self.angle)
        self.pub.publish(ld)

    def get_angle(self, angle_min, angle_inc, index):
        return angle_min + (angle_inc*index)

if __name__ == '__main__':
    dist = Distances(MIN_VALUE)
    #ai = AI(0.20)
    classes = list()
    classes.append(dist)
    listener(classes)





# class AI():
#     def __init__(self, limit):
#         self.pub = rospy.Publisher('moves', String, queue_size=1)
#         self.limit = limit

#     def find_move(self, dist):
#         move = ""
#         if dist.forward > self.limit:
#             move = "forward"
#         elif dist.left > self.limit:
#             move = "rot_left"
#         elif dist.right > self.limit:
#             move = "rot_right"
#         elif dist.backward > self.limit:
#             move = "backwardward"
#         else:
#             move = "rot_left"
#         return move

#     def edit_limit(self, limit):
#         self.limit = limit

#     def publish(self, string):
#         self.pub.publish(string)
