#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
import time
import math
import ConfigParser
from std_msgs.msg import String
from cringe_bot.msg import Sensordata
from cringe_bot.msg import IRdata

CALIBRATIONS = 15

def set_params(param):
	settings = ConfigParser.ConfigParser()
	settings.read("/home/ubuntu/Kommodul/parameters.conf")
	setting = settings.get("Parameters", param)
	return setting


def callback(data, args):
	ir1 = args[0]
	ir2 = args[1]
	pub = args[2]
	ir_read(ir, data.ir)
	ir_read(ir2, data.ir_right)
	irdat = IRdata(data.dist, ir1.hot, ir1.hot_boxes, ir2.hot, ir2.hot_boxes)
	pub.publish_ir(irdat)
	

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
		self.pub_ir = rospy.Publisher('ir', IRdata, queue_size=1)
		self.pub = rospy.Publisher('ir_info', String, queue_size=1)

	def publish_ir(self, ir):
		self.pub_ir.publish(ir)

	def publish_str(self, string):
		self.pub.publish(string)

class IR:
	def __init__(self, inits, temp_limit):
		self.init_reads = inits
		self.reads = self.init_reads
		self.ir_mean = 0.0
		self.first_temps = 0.0
		self.calibrated = False
		self.temp_limit = temp_limit
		self.hot = False
		self.hot_boxes = [0]*64

	def calibrate_mean(self, ir):
		temp_sum = 0.0
		for i in range(len(ir)):
		#	if not ((i % 8 == 5) or (i % 8 == 6) or (i % 8 == 7) or i == 4):
				temp_sum += ir[i]
		self.first_temps += temp_sum/64
		self.reads -= 1
		if self.reads == 0:
			self.calc_mean()

	def calc_mean(self):
		self.ir_mean = self.first_temps/self.init_reads
		self.calibrated = True

	def read_ir(self, ir):
		for i in range(len(ir)):
			if (i % 8 == 5) or (i % 8 == 6) or (i % 8 == 7) or i == 4:
				self.hot_boxes[i] = 0
			else:
				if ir[i] - self.ir_mean > self.temp_limit:
					self.hot_boxes[i] = 1
				else:
					self.hot_boxes[i] = 0
		if 1 in self.hot_boxes:
			self.hot = True
		else:
			self.hot = False

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

def zero_in_array(values):
	if any(v == 0 for v in values):
		return True
	else:
		return False

if __name__ == '__main__':
	TEMP_TRESH = set_params("Temperaturelimit")
	time.sleep(1)
	ir = IR(CALIBRATIONS, float(TEMP_TRESH))
	ir_2 = IR(CALIBRATIONS, float(TEMP_TRESH))
	dp = Distressed_publisher()
	args = list()
	args.append(ir)
	args.append(ir_2)
	args.append(dp)
	listener(args)
	#init_values = [20.0]*64
	#hot_values = init_values
	#hot_values[7] = 25.0
	#dist = 80.0
	#close_dist = 30.0
	#i = 0
	#while i < CALIBRATIONS:
	#	ir.calibrate_mean(init_values)
	#	i += 1
	#if ir.calibrated:
	#	ir.read_ir(hot_values)
	#	ir.read_dist(close_dist)
	#	print(str(ir.hot_boxes))
	#if ir.in_range and ir.hot:
	#	print("Yes")
	#else:
	#	print("No")
