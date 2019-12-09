#!/usr/bin/env python
from duckietown_msgs.msg import Twist2DStamped, LanePose
import sys
import math
import rospy
import time
from numpy import arange,sign

class pid_controller:
    def __init__(self):
        self.error_accum = 0
	self.error_phi = 0
        self.error_d = 0

	self.pub_control = rospy.Publisher("~car_cmd", Twist2DStamped, queue_size=1)
	self.sub_lanepose = rospy.Subscriber("~lane_pose", LanePose, self.pid_motion, queue_size=1)

	self.rate = rospy.Rate(10)
	self.lp = LanePose()
	self.tstart = None
    def pid_motion(self, lp):
	error_phi = 0
	error_d = 0
	control = 0
        kpphi = 1
	kpd = 1
	kiphi = 1
	kid = 1
    	kdphi = 1
    	kdd = 1
    	timep = self.tstart
    	twist = Twist2DStamped() 
	time = rospy.get_time()
        if timep != None:
    		dt = time - timep
    		error_d = 0 - lp.d
    		error_phi = 0 - lp.phi
    		self.error_acum += error_d*dt
    		integral = self.error_accum
    		if dt != 0:
    			derivative_d = (error_d - self.error_d)/dt
    			derivative_phi = (error_phi - self.error_phi)/dt
            	else:
                   	derivatived = 0.0
    			derivativephi = 0.0
        		controlphi = kpphi*error_phi + kdphi*derivative_phi + ki_phi*0.1
        		controlphi = max(min(control_phi,10.0), -10.0)
        		controld = kpd*error_d + kdd*derivative_d + kid*integral
        		controld = max(min(control_d,10.0), -10.0)
        		control = controlphi + controld

        		twist.omega = control
        		twist.v = 0.2


        		self.error_phi = error_phi
        		self.error_d = eroor_d
        		timep = t
        		self.t_start = t
            	self.t_start = t
            	self.pub_control.publish(twist)
	print("Error +", error_phi, error_d)
        print("Control", control)
if __name__ == "__main__":
		rospy.init_node("pid", anonymous=False)
		pid_node = pid_controller()
		rospy.spin()
