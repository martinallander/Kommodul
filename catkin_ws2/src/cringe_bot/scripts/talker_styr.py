#!/usr/bin/env python
# Software License Agreement (BSD License)

import time
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('spi_commands', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i = 0
    spi_str = "forward"
    while i < 8:
        if i == 4:
            spi_str = "backward"
        #time.sleep(5)
        rospy.loginfo(spi_str)
        pub.publish(spi_str)
        i += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
