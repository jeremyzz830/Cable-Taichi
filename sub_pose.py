#!/use/env/bin python

import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose

def callback(msg):

    pass

def plot_interp_3D():
    pass


def main():
    
        rospy.init_node('sub_pose')
        rospy.Subscriber('/NDI_plot', PoseStamped, callback)
        rospy.spin()


if __name__ == '__main__':
    main()
    