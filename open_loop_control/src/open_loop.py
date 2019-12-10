if __name__ == '__main__':
    rospy.init_node('open_loop', anonymous=True)
    pub = rospy.Publisher('~car_cmd', Twist2DStamped, queue_size=1)
    rate = rospy.Rate(10) # 10hz
    t_start = rospy.get_time()
    while not rospy.is_shutdown():
        t = rospy.get_time()
        msg = Twist2DStamped()
        dt = t - t_start
        if dt > 3 and dt < 6:
            msg.v = 0.50
            msg.omega = 0
        elif dt > 6 and dt < 8:
            msg.v = 0.10
            msg.omega = 1.0472
        elif dt > 8 and dt < 11:
            msg.v = 0.50
            msg.omega = 0.0
        elif dt > 11 and dt < 13:
            msg.v = 0.10
            msg.omega = 1.0472
        elif dt > 13 and dt < 16:
            msg.v = 0.50
            msg.omega = 0.0
        elif dt > 16 and dt < 18:
            msg.v = 0.10
            msg.omega = 1.0472
        elif dt > 18 and dt < 21:
            msg.v = 0.50
            msg.omega = 0.0
        elif dt > 21 and dt < 23:
            msg.v = 0.10
            msg.omega = 1.0472
        else:
            msg.v = 0
            msg.omega = 0
        pub.publish(msg)
        rate.sleep()
