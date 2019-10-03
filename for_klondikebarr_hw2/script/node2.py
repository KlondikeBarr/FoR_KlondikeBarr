#!/usr/bin/env python
import rospy
from for_klondikebarr_hw2.msg import Pos
from geometry_msgs.msg import Point
counter = 0
pub = rospy.Publisher('/registered_obstacle', Pos,queue_size=10)

def callback(data):
    global counter
    new_data = Pos()
    counter+=1
    new_data.id = str(counter)
    new_data.x = data.x
    new_data.y = data.y
    new_data.z = data.z
    print("I hear id: %s position: %f, %f, %f",new_data.id,new_data.x,new_data.y,new_data.z)
    pub.publish(new_data)
    rospy.sleep(.5) #wait for 1 sec

def listener():

    rospy.init_node('node2', anonymous=True)
    rospy.Subscriber("/obstacle_detection", Point, callback)


    rospy.spin()

if __name__ == '__main__':

    listener()
