#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
import time
from std_msgs.msg import String
from cringe_bot.msg import Sensordata

move_commands = ["rotright", "rotleft", "forward", "backward", "turnleft", "turnright"]

def callback(data, ir):
    if not zero_in_array(data.ir):
    	if ir.calibrated:
    		ir.read_ir(data.ir)
    		ir.read_dist(data.dist)
    	else:
    		ir.calibrate_mean(data.ir)
    

def listener(ir):
	rospy.init_node('distressed', anonymous=True)
	pub_moves = rospy.Publisher('moves', String, queue_size=1)
	rospy.Subscriber('sensor', Sensordata, callback, ir)
	rate = rospy.Rate(12) # 30hz
	while not rospy.is_shutdown():
		if ir.hot and ir.in_range:
			pub_moves.publish("Found")
		rate.sleep()
	rospy.spin()
	spi_node.close()

class IR:
	def __init__(self, inits, temp_limit, dist_limit):
		self.init_reads = inits
		self.reads = init_reads
		self.ir_mean = 0.0
		self.first_temps = 0.0
		self.calibrated = False
		self.temp_limit = temp_limit
		self.dist_limit = dist_limit
		self.hot = False
		self.in_range = False
		self.hot_boxes = list()

	def calibrate_mean(self, ir):
		for temp in ir:
			temp_sum += temp
		self.first_temps += temp_sum/64
		self.reads -= 1
		if self.reads == 0:
			self.calc_mean()

	def calc_mean(self):
		self.ir_mean = first_temps/self.init_reads
		self.calibrated = True

	def read_ir(self, ir):
		self.hot_boxes.clear()
		for i in range(len(ir)):
			if ir[i] - self.ir_mean > self.temp_limit:
				self.hot = True
				self.hot_boxes.append(i)
			else:
				self.hot = False

	def read_dist(self, dist):
		if dist < dist_limit:
			self.in_range = True
		else:
			self.in_range = False

def zero_in_array(values):
	if any(v == 0 for v in values):
		return True
	else:
		return False

if __name__ == '__main__': 
	ir = IR(10, 4.0, 50.0)
	listener(ir)