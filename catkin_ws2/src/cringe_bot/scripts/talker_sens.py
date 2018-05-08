#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('spi_commands', String, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz for ir
    while not rospy.is_shutdown():
	#rospy.loginfo("ir")
        pub.publish("ir")
	request(pub, rate)
	rate.sleep()

def request(pub, rate):
	for i in range(40):
            pub.publish("angle")
            pub.publish("acc")
            pub.publish("dist")
            

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
