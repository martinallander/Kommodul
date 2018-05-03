#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('spi_commands', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        spi_str = "ir"
        rospy.loginfo(spi_str)
        pub.publish(spi_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
