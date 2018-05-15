#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
import time
from std_msgs.msg import String
import math
from cringe_bot.msg import Sensordata

def callback(data, irs):
	ir1 = irs[0]
	ir2 = irs[1]
	ir_publish(ir, data.ir, data.dist, "forward")
	ir_publish(ir2, data.ir, data.dist, "right")

def ir_publish(ir, ir_data, dist, pub_str):
	if not zero_in_array(ir_data):
		if ir.calibrated:
			ir.read_ir(ir_data)
			ir.read_dist(dist)
		else:
			ir.calibrate_mean(ir_data)
	if ir.in_range and ir.hot:
		ir.publish(pub_str)
		ir.publish(str(ir.format_grid()))

def listener(ir):
	rospy.init_node('distressed', anonymous=True)
	rospy.Subscriber('sensor', Sensordata, callback, irs)
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
				self.hot_boxes.append(i)
				#print(i)
		if len(self.hot_boxes) == 0:
			self.hot = False
		else:
			self.hot = True

	def format_grid(self):
		boxes = list()
		if len(self.hot_boxes) == 0:
			return None
		else:
			for box in self.hot_boxes:
				boxes.append(self.index_to_coord(box))
			return boxes

	def index_to_coord(self, index):
		x = int(math.fabs(math.floor(index/8)-8))
		y = int(math.fabs((index % 8)-8))
		return(x,y)

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
	calibrations = 100
	temperature_threshold = 4.0
	distance_treshold = 50.0 
	ir = IR(calibrations, temperature_threshold, distance_treshold)
	ir_2 = IR(calibrations, temperature_threshold, distance_treshold)
	irs = list()
	irs.append(ir)
	irs.append(ir_2)
	listener(irs)
	#init_values = [20.0]*64
	#hot_values = init_values
	#hot_values[20] = 25.0
	#dist = 80.0
	#close_dist = 30.0
	#i = 0
	#while i < 11:
#		ir.calibrate_mean(init_values)
#		i += 1#
		#if ir.calibrated:
# 	ir.read_ir(hot_values)
# 	ir.read_dist(close_dist)
# 	grid = ir.format_grid()
# 	print(grid)
#	if ir.in_range and ir.hot:
#		print("Yes")
#	else:
#		print("No")
    #else:
