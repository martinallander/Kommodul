#!/usr/bin/env python

import math
from math import sin, cos, pi

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3
from std_msgs.msg import String

class Coord:
	def __init__(self, x, y ,th):
		self.x = x
		self.y = y
		self.th = th



def callback(data, coord):


	if data.data == "forward":
		#delta_x = 0.0723 * cos(coord.th) + 0.0 * sin(coord.th)
		#delta_y = -0.031 * sin(coord.th) - 0.0 * cos(coord.th)
		#delta_th = -0.004
		delta_x = 0.08 * cos(coord.th) + 0.0 * sin(coord.th)
		delta_y = 0.08 * sin(coord.th) - 0.0 * cos(coord.th)
		delta_th = -0.05 * pi /180
	elif data.data == "backward":
		#delta_x = - 0.0657 * cos(coord.th) + 0.0 * sin(coord.th)
		#delta_y = -0.0329 * sin(coord.th) + 0.0 * cos(coord.th)
		#delta_th = 0.00464
		delta_x = -0.07475 * cos(coord.th) + 0.0011875 * sin(coord.th)
		delta_y = -0.07475 * sin(coord.th) - 0.0011875 * cos(coord.th)
		delta_th = 0.46875 * pi /180
	elif data.data == "rotleft":
                delta_x = 0.0 * cos(coord.th) + 0.0 * sin(coord.th)
		delta_y = 0.0 * sin(coord.th) - 0.0 * cos(coord.th) 
		delta_th = 25 * pi /180
	elif data.data == "rotright":
		delta_x = 0.0 * cos(coord.th) - 0.0 * sin(coord.th)
		delta_y = 0.0 * sin(coord.th) + 0.0 * cos(coord.th)
		delta_th = -25 * pi /180
	elif data.data == "turnleft":
		delta_x = 0.081 * cos(coord.th) - 0.00925 * sin(coord.th)
		delta_y = 0.081 * sin(coord.th) + 0.00925 * cos(coord.th)
		delta_th = 1.5 * pi /180
	elif data.data == "turnright":
		delta_x = 0.074875 * cos(coord.th) + 0.007875 * sin(coord.th)
		delta_y = 0.074875 * sin(coord.th) - 0.007875 * cos(coord.th)
		delta_th = -1.75 * pi /180
	else:
		return None

	coord.x += delta_x
	coord.y += delta_y
	coord.th += delta_th

def main():
	rospy.init_node('odometry_publisher')

	coord = Coord(0.0, 0.0, 0.0)

	odom_pub = rospy.Publisher("odom", Odometry, queue_size = 50)
	odom_broadcaster = tf.TransformBroadcaster()
	rospy.Subscriber("moves", String, callback, coord)

	while not rospy.is_shutdown():
		current_time = rospy.Time.now()
		# since all odometry is 6DOF we'll need a quaternion created from yaw
		odom_quat = tf.transformations.quaternion_from_euler( 0 , 0 , coord.th)

		# first, we'll publish the transform over tf
		odom_broadcaster.sendTransform(
		(coord.x, coord.y, 0.),
		odom_quat,
		current_time,
		"base_link",
		"odom"
		)
		print(coord.x)

		# next, we'll publish the odometry message over ROS
		odom = Odometry()
		odom.header.stamp = current_time
		odom.header.frame_id = "odom"

		# set the position
		odom.pose.pose = Pose(Point(coord.x, coord.y, 0.), Quaternion( * odom_quat))

		# set the velocity
		odom.child_frame_id = "base_link"
		odom.twist.twist = Twist(Vector3(0, 0, 0 ), Vector3( 0 , 0 , 0)) #Velocities =0

		# publish the message
		odom_pub.publish(odom)

		rospy.sleep()
		pass

if __name__ == '__main__':
	main()
