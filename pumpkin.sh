#!/bin/bash
MASTER=$HOSTNAME
cd ~/workspace/pumpkin_ws/
source devel/setup.bash
export ROS_MASTER_URI=http://$MASTER:11311
#roslaunch pumpkin pumpkin.launch
roslaunch pumpkin pumpkin_kinect.launch
rosrun pumpkin head_init.py
