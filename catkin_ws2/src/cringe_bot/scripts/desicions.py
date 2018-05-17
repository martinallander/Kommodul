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
    rate = rospy.Rate(1)
    while not rospy.is_shutdown() and not AI.found:
        AI.decide()
        rate.sleep()
    rospy.spin()

class AI():
    def __init__(self):
        self.pub = rospy.Publisher('spi_commands', String, queue_size=1)
        self.forward = False
        self.backward = False
        self.left = False
        self.right = False
        self.found = False
        self.turn_right = False
        self.turn_left = False
        self.allowed = [0] * 64
        self.has_forward = False
        self.has_right = False
        self.ir_forward = [0] * 64
        self.ir_right = [0] * 64
        self.queue = list()

    def publish(self, string):
        self.pub.publish(string)

    def decide(self):
    	available_commands = self.possible()
    	prefered_commands = self.prefered()
    	for move in prefered_commands:
    		if move in available_commands:
    			command = move
    	self.publish(move)

    def camera_placement(self, ir):
    	placement = list()
    	for i in range(15,47):
    		if ir[i] == 1:
    			placement.append("middle")
    	for i in range(47,63):
    		if ir[i] == 1:
    			placement.append("left")
    	for i in range(0,15):
    		if ir[i] == 1:
    			placement.append("right")
    	return placement

    def prefered(self):
    	preferences = list()
    	if self.has_forward:
    		placement = self.camera_placement(self.ir_forward)
    		if "forward" in placement:
    			preferences.append("forward")
    		if "left" in placement:
    			preferences.append("turnleft")
    		if "right" in placement:
    			preferences.append("turnright")
    	if self.has_right:
    			preferences.append("rotright")
    	preferences.append("forward")
    	preferences.append("turnleft")
    	preferences.append("turnright")
    	preferences.append("backward")
    	preferences.append("rotright")
    	preferences.append("rotleft")
    	return preferences


    def possible(self):
    	available_commands = list()
    	if self.forward:
    		available_commands.append("forward")
    	if self.turn_right:
    		available_commands.append("turnright")
    	if self.backward:
    		available_commands.append("backward") 
    	if self.turn_left:
    		available_commands.append("forward")
    	available_commands.append("rotright")
    	available_commands.append("rotleft")
    	return available_commands


    def get_lidar(self,lidar):
        self.forward = lidar.forward
        self.backward = lidar.backward
        self.right = lidar.right
        self.left = lidar.left
        self.turn_right = lidar.turn_right
        self.turn_left = lidar.turn_left
        self.allowed = lidar.minimum

    def get_distressed(self,irdata):
        self.found = irdata.found
        self.has_forward = irdata.has_forward
        self.ir_forward = irdata.ir_forward
        self.has_right = irdata.has_right
        self.ir_right = irdata.ir_right

    def index_to_coord(self, index):
		x = int(math.fabs(math.floor(index/8)-8))
		y = int(math.fabs((index % 8)-8))
		return(x,y)


if __name__ == '__main__':
    ai = AI()
    listener(ai)

