#!/usr/bin/env python
# Software License Agreement (BSD License)

from SPI import SPI
import rospy
import time
from std_msgs.msg import String
from cringe_bot.msg import Sensordata

move_commands = ["rotright", "rotleft", "forward", "backward", "turnleft", "turnright"]

def callback(data, spi_node):
    if data.data.lower() in move_commands:
        spi_node.insert_styr_back(data.data.lower())
	spi_node.perform_action()
    

def listener(spi_node):
	rospy.init_node('spi_node', anonymous=True)
	pub_sensor = rospy.Publisher('sensor', Sensordata, queue_size=1)
	pub_moves = rospy.Publisher('moves', String, queue_size=1)
	rospy.Subscriber('spi_commands', String, callback, spi_node)
	rate = rospy.Rate(12) # 30hz
	while not rospy.is_shutdown():
		spi_node.perform_action()
		last_move = spi_node.spi.publish_move()
		if last_move != None:
			pub_moves.publish(last_move)
		sd = Sensordata(spi_node.spi.sd.acc, spi_node.spi.sd.angle, spi_node.spi.sd.ir, spi_node.spi.sd.tof)
		pub_sensor.publish(sd)
		rate.sleep()
	rospy.spin()
	spi_node.close()

class SPI_node:
	def __init__(self):
		self.spi = SPI(150000)
		self.styr_queue = list()
		self.sens_queue = list()

	def insert_sens_back(self, data):
		self.sens_queue.append(data)

	def insert_sens_front(self, data):
		self.sens_queue = [data.data] + spi_node.sens_queue

	def insert_styr_back(self, data):
		self.styr_queue.append(data)

	def insert_styr_front(self, data):
		self.styr_queue = [data.data] + spi_node.sens_queue

	def perform_action(self):
		if(self.spi.done == True):
			if not len(self.styr_queue) == 0:  
				if  self.spi.move(self.styr_queue[0]):
					self.styr_queue.pop(0)
			else:
				self.spi.read("acc")
				self.spi.read("angle")
				self.spi.read("dist")
				self.spi.read("ir")

	def close(self):
		self.spi.sens.close()
		self.spi.styr.close()

if __name__ == '__main__': 
	print("Starting!")
	sp = SPI_node()
	listener(sp)
