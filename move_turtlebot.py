#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/cmd_vel_mux/input/navi', Twist, queue_size=1)
rate = rospy.Rate(2)
move = Twist() # defining the way we can allocate the values
move.linear.x = 0.5 # allocating the values in x direction - linear
move.angular.z = 0.5  # allocating the values in z direction - angular

while not rospy.is_shutdown(): 
  pub.publish(move)
  rate.sleep()