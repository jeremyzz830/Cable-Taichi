import rospy

def mian():
    rospy.init_node('cube_listener')
    rospy.Subscriber('/cube', Float64, callback)
    rospy.spin()

    pass