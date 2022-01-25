#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray

def cb(message):
   n = (len(message.data) - 1)
   print (n)

if __name__ == '__main__': 
        rospy.init_node('factorization')
        sub = rospy.Subscriber('Prime_list', Int32MultiArray,cb)
        rate = rospy.Rate(10)
        rospy.spin()




