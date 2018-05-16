#!/usr/bin/env python

import time
import os

time.sleep(5)

path = "catkin_ws2/"

os.chdir(path)
os.system("source devel/setup.bash")
os.system("roslaunch rplidar_ros theoslam.launch")
