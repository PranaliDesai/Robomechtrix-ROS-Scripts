#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def subscriberCallBack(data):
    rospy.loginfo(rospy.get_caller_id() + " I recieved --  %s", data.data) #prints on terminal
    
def listener():
    rospy.init_node('subscriberNode', anonymous=True)
    rospy.Subscriber("talker", String, subscriberCallBack)
    rospy.spin() # the python file does not exit

if __name__ == '__main__':
    listener()