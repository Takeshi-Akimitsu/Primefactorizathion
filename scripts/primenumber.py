#!/usr/bin/env python3                                                                       
import rospy 
from std_msgs.msg import Int32MultiArray

rospy.init_node('prime')
pub = rospy.Publisher('Prime_list', Int32MultiArray, queue_size=10)
rate = rospy.Rate(10)

print('Prease input a number:',end = ' ') 
n = int(input()) 

while not rospy.is_shutdown():
    prime_list=[]
    prime_list.append(n)
    for i in range(2,n+1):
        prime_list.append(i)
        for p in range(2,i):
            if i % p == 0:
             prime_list.remove(i)
             break

        array_forPublish = Int32MultiArray(data=prime_list)

    pub.publish(array_forPublish)
    rate.sleep()
#print(prime(n))
