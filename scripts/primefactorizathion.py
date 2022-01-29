#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String

s = 0

def cb(prime):
    prime_list = list(prime.data)
    n = prime_list[len(prime_list)-1]
    m = prime_list[len(prime_list)-2]
    prime_list.remove(n)
    global s

    
    if n == m & n == 0:
        s = ('{0} is not primenumber'.format(n))

    elif n == m & n == 1:
        s = ('{0} is not primenumber'.format(n))

    elif n == m:
        s = ('{0} is primenumber'.format(n))

    else:
        l = n
        number = []

        for x in range(0,len(prime_list)-1):
            while True:
                if n % prime_list[x] == 0:
                    n = n / prime_list[x]
                    number.append(prime_list[x])
                else:
                    x = x + 1
                    break

        number1 = []
        number2 = []

        for y in range(0,len(number)-1):
            if y == 0:
                number1.append(number.count(number[y]))
                number2.append(number[y])

            elif number[y] == number[0]:
                y = y + 1

            elif number[y] == number[y + 1] & number[y] != number[y - 1]:
                number1.append(number.count(number[y]))
                number2.append(number[y])

            elif number[y] != number[y + 1] & number[y] != number[y - 1]:
                number1.append(number.count(number[y]))
                number2.append(number[y])
    
        if number.count(number[len(number)-1]) == 1:
            number1.append(1)
            number2.append(number[len(number)-1])
        
        number1 = list(map(str,number1))
        number2 = list(map(str,number2))

        primefactorizathion_list = [*map("^".join,zip(number2,number1))]

        answer = '*'.join(primefactorizathion_list)

        s = ('{0} = {1}'.format(l,answer))

if __name__ == '__main__': 
        rospy.init_node('primefactorizathion')
        sub = rospy.Subscriber('prime_list', Int32MultiArray, cb)
        pub = rospy.Publisher('primefactorizathion', String, queue_size=10)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            pub.publish(str(s))
            rate.sleep()
