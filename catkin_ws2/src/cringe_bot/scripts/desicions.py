#!/usr/bin/env python
# Software License Agreement (BSD License)

import random
import operator
import os
import rospy
from std_msgs.msg import String
from cringe_bot.msg import IRdata
from cringe_bot.msg import Lidardistances

FORWARD = "forward"
BACKWARD = "backward"
TURNLEFT = "turnleft"
TURNRIGHT = "turnright"
ROTRIGHT = "rotright"
ROTLEFT = "rotleft"


def callback(lidar, ai):
    ai.get_lidar(lidar)
    #ai.publish(str(lidar.backward))
    #ai.publish(str(lidar.minimum))
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
	rate = rospy.Rate(0.5)
	while not rospy.is_shutdown():
		#AI.pubinfo()
		#rate.sleep()
		AI.pubinfo()
		AI.decide()
		rate.sleep()
	rospy.spin()

class AI():
	def __init__(self):
		self.pub = rospy.Publisher('spi_commands', String, queue_size=1)
		self.pubfound = rospy.Publisher('info', String, queue_size=1)
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
		self.prev = ""
		self.queue = list()

	def publish(self, string):
		self.pub.publish(string)
	
	def pubdist(self, string):
		self.pubfound.publish(string)

	def pubinfo(self):
		self.pubdist("Found: " + str(self.found))
		self.pubdist("Hot forward: " + str(self.has_forward))
		self.pubdist("Hot right : " + str(self.has_right))

	def prefered(self):
		preferences = list()
		if self.has_forward:
			placement = self.camera_placement(self.ir_forward)
			if "middle" in placement:
				preferences.append(FORWARD)
			if "left" in placement:
				preferences.append(TURNLEFT)
			if "right" in placement:
				preferences.append(TURNRIGHT)
		#if self.has_right:
			#preferences.append(TURNRIGHT)
			#self.queue.append(TURNRIGHT)
		preferences.append(FORWARD)
		preferences.append(TURNLEFT)
		preferences.append(TURNRIGHT)
		if self.prev == ROTRIGHT or ROTLEFT:
			preferences.append(self.prev)
		if self.right and self.left:
			pick = random.choice([True, False])
			if pick:
				preferences.append(ROTRIGHT)
			else:
				preferences.append(ROTLEFT)
		if self.right:
			preferences.append(ROTRIGHT)
		if self.left:
			preferences.append(ROTLEFT)
		else:
			pick = random.choice([True, False])
			if pick:
				preferences.append(ROTRIGHT)
			else:
				preferences.append(ROTLEFT)
		preferences.append(BACKWARD)
		return preferences

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

	def available(self):
		available_commands = list()
		if self.forward:
			available_commands.append(FORWARD)
		if self.turn_right:
			available_commands.append(TURNRIGHT)
		if self.backward:
			available_commands.append(BACKWARD) 
		if self.turn_left:
			available_commands.append(TURNLEFT)
		available_commands.append(ROTRIGHT)
		available_commands.append(ROTLEFT)
		return available_commands

	def decide(self):
		command = ""
		available_commands = self.available()
		prefered_commands = self.prefered()
		if not len(self.queue) == 0 and self.prev == ROTRIGHT:
			prefered_commands.insert(0, self.queue.pop(0))
		for i in range(len(prefered_commands)):
			if prefered_commands[i] in available_commands:
				command = prefered_commands[i]
				break
		#self.publish(str(prefered_commands))
		#self.publish(command)
		self.pubdist(str(available_commands))
		self.prev = command

	def get_lidar(self, lidar):
		self.forward = lidar.forward
		self.backward = lidar.backward
		self.right = lidar.right
		self.left = lidar.left
		self.turn_right = lidar.turn_right
		self.turn_left = lidar.turn_left
		self.allowed = lidar.minimum

	def get_distressed(self, irdata):
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

