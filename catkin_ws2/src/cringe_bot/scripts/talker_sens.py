#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('spi_commands', String, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(530) # 10hz for ir
    while not rospy.is_shutdown():
        for i in range(40):
            spi_str = "angle"
            pub.publish(spi_str)
            spi_str = "acc"
            pub.publish(spi_str)
            spi_str = "dist"
            pub.publish(spi_str)
            rate.sleep()
        spi_str = "ir"
        pub.publish(spi_str)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
