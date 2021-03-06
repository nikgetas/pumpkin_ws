#!/usr/bin/env python
# coding: utf-8
import sys
import rospy
import copy
import geometry_msgs.msg
import moveit_msgs.msg

from moveit_commander import RobotCommander, MoveGroupCommander
from moveit_commander import PlanningSceneInterface, roscpp_initialize, roscpp_shutdown

from math import sin, copysign, sqrt, pi
   
if __name__ == '__main__':
    print "============ Dynamic hand gestures: Come"
    roscpp_initialize(sys.argv)
    rospy.init_node('pumpkin_planning', anonymous=True)

    right_arm = MoveGroupCommander("right_arm")
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
    print right_arm.get_current_pose().pose

    wpose = geometry_msgs.msg.Pose()
    wpose.orientation.w = 0.409003402335
    wpose.orientation.x = -0.330487715391
    wpose.orientation.y = -0.782324118504
    wpose.orientation.z = -0.333860839963
    wpose.position.y = 0.0776977107894
    wpose.position.z = 1.25950497489
    wpose.position.x = -0.199191527741
    right_arm.set_pose_target(wpose)
    plan1 = right_arm.plan()

    right_arm.execute(plan1)
    print "============ Waiting while RVIZ executes plan1..."
    rospy.sleep(5)
    waypoints = []
    waypoints.append(right_arm.get_current_pose().pose)
    print right_arm.get_current_pose().pose
    

    points = 20
    for i in xrange(points):
        wpose = geometry_msgs.msg.Pose()
        wpose.orientation.w = waypoints[i-1].orientation.w + 0.428513
        wpose.orientation.x = waypoints[i-1].orientation.x 
        wpose.orientation.y = waypoints[i-1].orientation.y 
        wpose.orientation.z = waypoints[i-1].orientation.z - 0.175202
        wpose.position.y = waypoints[i-1].position.y - 0.025
        wpose.position.z = waypoints[i-1].position.z + 0.25
        wpose.position.x = waypoints[i-1].position.x - 0.0218657
        
        waypoints.append(copy.deepcopy(wpose))

    
    (come, fraction) = right_arm.compute_cartesian_path(
                                                         waypoints,   # waypoints to follow
                                                         0.01,        # eef_step
                                                         0.0)         # jump_threshold
    
    print "============ Waiting while RVIZ displays come..."
    rospy.sleep(5)
    right_arm.execute(come)

    roscpp_shutdown()