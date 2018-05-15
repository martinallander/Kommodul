#!/usr/bin/env python
# Software License Agreement (BSD License)

import rospy
from std_msgs.msg import String
from cringe_bot.msg import Sensordata

init_values = [20.0]*64
hot_values = init_values
hot_values[20] = 25.0
dist = 80.0
close_dist = 30.0

def talker():
    pub = rospy.Publisher('sensor', Sensordata, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i = 0
    while not rospy.is_shutdown():
        if i > 10:
            sd = Sensordata([0.0,0.0,0.0], [0.0,0.0,0.0], hot_values, hot_values, close_dist)
        #if i == 14:
        #    sd = Sensordata([0.0,0.0,0.0], [0.0,0.0,0.0], hot_values, dist)
        #if i == 15:
        #    sd = Sensordata([0.0,0.0,0.0], [0.0,0.0,0.0], hot_values, close_dist)
            i = 0
        sd = Sensordata([0.0,0.0,0.0], [0.0,0.0,0.0], init_values, init_values, dist)
        #rospy.loginfo(sd)
        pub.publish(sd)
        rate.sleep()
        i += 1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
