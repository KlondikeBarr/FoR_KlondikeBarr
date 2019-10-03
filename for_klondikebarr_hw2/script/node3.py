#!/usr/bin/env python
import rospy
from for_klondikebarr_hw2.msg import Pos
from geometry_msgs.msg import Point

def callback(data):
    rospy.loginfo('Detected obstacle %s at position %f,%f,%f',data.id,data.x,data.y,data.z)

def listener():

    rospy.init_node('node3', anonymous=True)
    rospy.Subscriber("/registered_obstacle", Pos, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
