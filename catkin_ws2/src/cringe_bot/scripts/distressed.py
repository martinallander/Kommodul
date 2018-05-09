#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
import time
from std_msgs.msg import String
from cringe_bot.msg import Sensordata

def callback(data, ir):
    if not zero_in_array(data.ir):
    	if ir.calibrated:
    		ir.read_ir(data.ir)
    		ir.read_dist(data.dist)
    	else:
    		ir.calibrate_mean(data.ir)
    if ir.in_range and ir.hot:
    	ir.publish("Yes")
    else:
    	ir.publish("NO")

def listener(ir):
	rospy.init_node('distressed', anonymous=True)
	rospy.Subscriber('sensor', Sensordata, callback, ir)
	rospy.spin()

class IR:
	def __init__(self, inits, temp_limit, dist_limit):
		self.init_reads = inits
		self.reads = self.init_reads
		self.ir_mean = 0.0
		self.first_temps = 0.0
		self.calibrated = False
		self.temp_limit = temp_limit
		self.dist_limit = dist_limit
		self.hot = False
		self.in_range = False
		self.hot_boxes = list()
		self.pub_moves = rospy.Publisher('moves', String, queue_size=1)

	def calibrate_mean(self, ir):
		temp_sum = 0.0
		for temp in ir:
			temp_sum += temp
		self.first_temps += temp_sum/64
		self.reads -= 1
		if self.reads == 0:
			self.calc_mean()

	def calc_mean(self):
		self.ir_mean = self.first_temps/self.init_reads
		self.calibrated = True

	def read_ir(self, ir):
		self.hot_boxes[:] = []
		for i in range(len(ir)):
			if ir[i] - self.ir_mean > self.temp_limit:
				self.hot = True
				self.hot_boxes.append(i)
			else:
				self.hot = False

	def read_dist(self, dist):
		if dist < self.dist_limit:
			self.in_range = True
		else:
			self.in_range = False

	def publish(self, string):
		self.pub_moves.publish(string)

def zero_in_array(values):
	if any(v == 0 for v in values):
		return True
	else:
		return False

if __name__ == '__main__': 
	ir = IR(10, 4.0, 50.0)
	listener(ir)