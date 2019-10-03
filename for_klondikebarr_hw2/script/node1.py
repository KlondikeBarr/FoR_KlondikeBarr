#!/usr/bin/env python
#import roslib; roslib.load_manifest('for_klondikebarr_hw2')
import rospy
import random
from geometry_msgs.msg import Point

def talker():
  pub = rospy.Publisher('obstacle_detection', Point,queue_size=10)
  rospy.init_node('node1')

  while not rospy.is_shutdown():
    point = Point()
    point.x = random.uniform(1,10)
    point.y = random.uniform(1,10)
    point.z = random.uniform(1,10)
    pub.publish(point)
    rospy.sleep(1.0)


if __name__ == '__main__':
  try:
    talker()
  except rospy.ROSInterruptException: pass
