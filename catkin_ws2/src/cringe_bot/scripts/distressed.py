#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
import time
from std_msgs.msg import String
import math
from cringe_bot.msg import Sensordata
from cringe_bot.msg import IRdata

CALIBRATIONS = 10
TEMP_TRESH = 4.0
DIST_TRESH = 50.0

def callback(data, args):
	ir1 = args[0]
	ir2 = args[1]
	pub = args[2]
	ir_read(ir, data.ir)
	ir_read(ir2, data.ir_right)
	if (data.dist - ir1.dist_limit) < 0:
		found = True
	else:
		found = False
	pub.publish(found, ir1.hot, ir1.hot_boxes, ir2.hot, ir2.hot_boxes)

def ir_read(ir, ir_data):
	if not zero_in_array(ir_data):
		if ir.calibrated:
			ir.read_ir(ir_data)
		else:
			ir.calibrate_mean(ir_data)

def listener(args):
	rospy.init_node('distressed', anonymous = True)
	rospy.Subscriber('sensor', Sensordata, callback, args)
	rospy.spin()

class Distressed_publisher():
	def __init__(self):
		self.pub_ir = rospy.Publisher('distressed', IRdata, queue_size=1)

	def publish(self, found, has_forward, ir_forward, has_right, ir_right):
		pub = IRdata(found, has_forward, ir_forward, has_right, ir_right)
		self.pub_ir.publish(pub)

class IR:
	def __init__(self, inits, temp_limit, dist_limit = 0.0):
		self.init_reads = inits
		self.reads = self.init_reads
		self.ir_mean = 0.0
		self.first_temps = 0.0
		self.calibrated = False
		self.temp_limit = temp_limit
		self.dist_limit = dist_limit
		self.hot = False
		self.in_range = False
		self.hot_boxes = [0]*64

	def calibrate_mean(self, ir):
		temp_sum = 0.0
		for temp in ir:
			temp_sum += temp
		self.first_temps += temp_sum/64
		self.reads -= 1
		print(self.reads)
		if self.reads == 0:
			self.calc_mean()

	def calc_mean(self):
		self.ir_mean = self.first_temps/self.init_reads
		self.calibrated = True

	def read_ir(self, ir):
		for i in range(len(ir)):
			if ir[i] - self.ir_mean > self.temp_limit:
				self.hot_boxes[i] = 1
			else:
				self.hot_boxes[i] = 0
		if 1 in self.hot_boxes:
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


def zero_in_array(values):
	if any(v == 0 for v in values):
		return True
	else:
		return False

if __name__ == '__main__':
	calibrations = 10
	temperature_threshold = 4.0
	distance_treshold = 50.0 
	ir = IR(calibrations, temperature_threshold, distance_treshold)
	ir_2 = IR(calibrations, temperature_threshold)
	dp = Distressed_publisher()
	args = list()
	args.append(ir)
	args.append(ir_2)
	args.append(dp)
	listener(args)
	# init_values = [20.0]*64
	# hot_values = init_values
	# hot_values[20] = 25.0
	# dist = 80.0
	# close_dist = 30.0
	# i = 0
	# while i < 11:
	# 	ir.calibrate_mean(init_values)
	# 	i += 1#
	# if ir.calibrated:
	# 	print("Cal")
	# 	ir.read_ir(hot_values)
	# 	ir.read_dist(close_dist)
	# 	grid = ir.format_grid()
	# 	print(grid)
	# if ir.in_range and ir.hot:
	# 	print("Yes")
	# else:
	# 	print("No")
    #else:
