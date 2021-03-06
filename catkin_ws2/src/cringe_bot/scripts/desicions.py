#!/usr/bin/env python
# Software License Agreement (BSD License)

import time
import random
import operator
import os
import rospy
import RPi.GPIO as GPIO
import ConfigParser
import pigpio
from std_msgs.msg import String
from cringe_bot.msg import IRdata
from cringe_bot.msg import Lidardistances

DIST_TRESH = 50.0

FORWARD = "forward"
BACKWARD = "backward"
TURNLEFT = "turnleft"
TURNRIGHT = "turnright"
ROTRIGHT = "rotright"
ROTLEFT = "rotleft"

move_commands = [FORWARD, BACKWARD, TURNLEFT, TURNRIGHT, ROTRIGHT, ROTLEFT]

pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)

def set_params(param):
	settings = ConfigParser.ConfigParser()
	settings.read("/home/ubuntu/Kommodul/parameters.conf")
	setting = settings.get("Parameters", param)
	return setting

def callback(lidar, ai):
    ai.get_lidar(lidar)

def callback_dist(irdata, ai):
    ai.get_distressed(irdata)

def callback_gui(guidata, ai):
	if guidata.data in move_commands and not ai.autonomous:
		ai.publish(guidata.data)
	elif guidata.data == "Autonom":
		ai.autonomous = True
		#AI.pubdist("Autonom")
	elif guidata.data == "Manual":
		ai.autonomous = False
		#AI.pubdist("Manual")

def closest(values):
    return min(values)

def LED_on():
	pi.write(17, 1)

def LED_off():
	pi.write(17, 0)

def mini_range(values):
    min_index, min_value = min(enumerate(values), key=operator.itemgetter(1))
    return [min_index, min_value]

def listener(AI):
	rospy.init_node('ai', anonymous=True)
	rospy.Subscriber('lidar_data', Lidardistances, callback, AI)
	rospy.Subscriber('ir', IRdata, callback_dist, AI)
	rospy.Subscriber('gui_info', String, callback_gui, AI)
	rate = rospy.Rate(1)
	LED_off()
	while not rospy.is_shutdown():
		AI.check_found()
		if AI.found:
			LED_on()
			time.sleep(5)
			AI.pubdist("Done")
			LED_off()
			pi.stop()
			break
		if not AI.found:
			AI.decide()
		rate.sleep()
	rospy.spin()

class AI():
	def __init__(self, dist):
		self.pub = rospy.Publisher('spi_commands', String, queue_size=1)
		self.pubfound = rospy.Publisher('info', String, queue_size=1)
		self.forward = False
		self.backward = False
		self.left = False
		self.right = False
		self.found = False
		self.turn_right = False
		self.turn_left = False
		self.allowed = [0] * 360
		self.has_forward = False
		self.has_right = False
		self.ir_forward = [0] * 64
		self.ir_right = [0] * 64
		self.prev = ""
		self.queue = list()
		self.lit = False
		self.dist = dist
		self.moves_done = list()
		self.lidar_dist = False
		self.autonomous = False

	def publish(self, string):
		self.pub.publish(string)

	def pubdist(self, string):
		self.pubfound.publish(string)

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
			if "middle" in placement:
				preferences.append(FORWARD)
			if "left" in placement:
				preferences.append(TURNLEFT)
			if "right" in placement:
				preferences.append(TURNRIGHT)
		if self.has_right:
			preferences.append(ROTRIGHT)
			self.queue.append(ROTRIGHT)
		if self.right == False and self.left:
			pick = random.choice([True, False])
			if pick:
				preferences.append(FORWARD)
			else:
				preferences.append(TURNLEFT)
		if self.right and self.left == False:
			pick = random.choice([True, False])
			if pick:
				preferences.append(FORWARD)
			else:
				preferences.append(TURNRIGHT)
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
		if self.autonomous:
			self.publish(command)
			self.prev = command
		self.pubdist(str(available_commands))

	def inverse_move(self, move):
		inverse = ""
		if move == FORWARD or TURNLEFT or TURNRIGTH:
			inverse = BACKWARD
		if move == BACKWARD:
			inverse = FORWARD
		if move == ROTRIGHT:
			inverse = ROTLEFT
		if move == ROTLEFT:
			inverse = ROTRIGHT
		return inverse

	def move_back(self):
		latest_move = self.moves_done[-1]
		self.moves_done.pop(-1)
		inverse = self.inverse_move(latest_move)
		return inverse

	def get_lidar(self, lidar):
		self.forward = lidar.forward
		self.backward = lidar.backward
		self.right = lidar.right
		self.left = lidar.left
		self.turn_right = lidar.turn_right
		self.turn_left = lidar.turn_left
		self.allowed = lidar.minimum
		self.lidar_dist = lidar.distressed

	def get_distressed(self, irdata):
		if not self.found:
			self.dist = irdata.dist
			self.has_forward = irdata.has_forward
			self.ir_forward = irdata.ir_forward
			self.has_right = irdata.has_right
			self.ir_right = irdata.ir_right
		else:
			self.pubdist("Found")
			self.found = True
			self.dist = 1000.0
			self.has_forward = False
			self.has_right = False
			self.ir_forward = irdata.ir_forward
			self.ir_right = irdata.ir_right

	def check_found(self):
		if self.lidar_dist and self.has_forward:
			self.found = True
		else:
			self.found = False

	def index_to_coord(self, index):
		x = int(math.fabs(math.floor(index/8)-8))
		y = int(math.fabs((index % 8)-8))
		return(x,y)

if __name__ == '__main__':
	try:
		DIST = set_params("Distresseddistance")
		ai = AI(float(DIST))
		listener(ai)
	except rospy.ROSInterruptException:
		LED_off()
		pi.stop()
		

