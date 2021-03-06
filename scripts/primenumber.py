#!/usr/bin/env python3                                                                       
import rospy 
from std_msgs.msg import Int32MultiArray

rospy.init_node('prime')
pub = rospy.Publisher('primenumber', Int32MultiArray, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    print('Prease input a number:',end = ' ')
    n = int(input())
    prime_list = []

    if n == 0 or n ==1:
        prime_list = [n]

    else:
        for i in range(2,n+1):
            prime_list.append(i)
            for j in range(2,i):
                if i % j == 0:
                    prime_list.remove(i)
                    break

    prime_list.append(n)

    prime = Int32MultiArray(data=prime_list)
    
    pub.publish(prime)
    rate.sleep()


