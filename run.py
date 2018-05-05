import time
import os

time.sleep(10)

path = "catkin_ws2/"

os.chdir(path)
os.system("source devel/setup.bash")
os.system("roslaunch cringe_bot cringe.launch")
