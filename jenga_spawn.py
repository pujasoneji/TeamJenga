"""
Jenga - Full Tower
"""
import argparse
import struct
import sys
import copy

import rospy
import rospkg

from gazebo_msgs.srv import (SpawnModel, DeleteModel)
from geometry_msgs.msg import (PoseStamped, Pose, Point, Quaternion)
from std_msgs.msg import (Header, Empty)

from baxter_core_msgs.srv import (SolvePositionIK, SolvePositionIKRequest)

import baxter_interface

import tf


# Spawning table with predefined pose
def spawn_gazebo_table(table_pose=Pose(position=Point(x=0.95, y=0.0, z=0.0)),
                       table_reference_frame="world"):

    # Load Table SDF
    table_xml = ''
    with open ("models/cafe_table/model.sdf", "r") as table_file:
        table_xml=table_file.read().replace('\n', '')

    # Spawn Table SDF
    rospy.wait_for_service('/gazebo/spawn_sdf_model')
    try:
        spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        resp_sdf = spawn_sdf("cafe_table", table_xml, "/",
                             table_pose, table_reference_frame)
    except rospy.ServiceException, e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))

# Spawning brick with predefined pose
def spawn_gazebo_brick(brick_pose,
                       brick_reference_frame="world",
                       count=1):

    # Load Brick SDF
    brick_xml = ''
    with open ("models/brick/model.sdf", "r") as brick_file:
        brick_xml=brick_file.read().replace('\n', '')

     # Spawn Brick SDF
    rospy.wait_for_service('/gazebo/spawn_sdf_model')

    try:

        if (count == 1):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick1", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 2): 
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick2", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 3):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick3", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 4):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick4", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 5):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick5", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 6):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick6", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 7):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick7", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 8):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick8", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 9):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick9", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 10):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick10", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

        elif (count == 11):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick11", brick_xml, "/",
                                 brick_pose, brick_reference_frame)  

        elif (count == 12):
            spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
            resp_sdf = spawn_sdf("brick12", brick_xml, "/",
                                 brick_pose, brick_reference_frame)

    except rospy.ServiceException, e:
        rospy.logerr("Spawn SDF service call failed: {0}".format(e))

# Deleting models from gazebo
def delete_gazebo_models():
    try:
        delete_model = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        resp_delete = delete_model("cafe_table")
        resp_delete = delete_model("brick1")
        resp_delete = delete_model("brick2")
        resp_delete = delete_model("brick3")
        resp_delete = delete_model("brick4")
        resp_delete = delete_model("brick5")
        resp_delete = delete_model("brick6")
        resp_delete = delete_model("brick7")
        resp_delete = delete_model("brick8")
        resp_delete = delete_model("brick9")
        resp_delete = delete_model("brick10")
        resp_delete = delete_model("brick11")
        resp_delete = delete_model("brick12")
    except rospy.ServiceException, e:
        rospy.loginfo("Delete Model service call failed: {0}".format(e))

def main():
    '''
    OFFSET VARIABLES
    '''
    hover_distance = 0.1 # meters

    # Define offset - original table sdf was 0.82 for base(0.04) + column(0.04) + surface(0.74)
    off = 0.32

    # Trim for how close brick can go from gazebo to real world
    trim = 0


    '''
    ORIENTATITIONS
    '''
    # This orientation matches that of 'tuck_arms.py -u'
    roll1 = 3.14159265359
    pitch1 = 0
    yaw1 = -3.14159265359
    quat1 = tf.transformations.quaternion_from_euler(roll1, pitch1, yaw1)

    # rotate end-effector 90 degrees about z
    roll2 = 3.14159265359
    pitch2 = 0
    yaw2 = -1.57079632679
    quat2 = tf.transformations.quaternion_from_euler(roll2, pitch2, yaw2)

    '''
    PLACING POSES
    '''
    # Place pose 1
    place_pose1 = Pose()
    place_pose1.position.x = 0.589679836383
    place_pose1.position.y = 0.0
    place_pose1.position.z = 0.183676720426 - off
    place_pose1.orientation.x = quat1[0]
    place_pose1.orientation.y = quat1[1]
    place_pose1.orientation.z = quat1[2]
    place_pose1.orientation.w = quat1[3]

    # Place pose 2 (x + 0.07)
    place_pose2 = Pose()
    place_pose2.position.x = 0.659679836383 - trim
    place_pose2.position.y = 0.0
    place_pose2.position.z = 0.183676720426 - off
    place_pose2.orientation.x = quat1[0]
    place_pose2.orientation.y = quat1[1]
    place_pose2.orientation.z = quat1[2]
    place_pose2.orientation.w = quat1[3]

    # Place pose 3
    place_pose3 = Pose()
    place_pose3.position.x = 0.729679836383 - 2*trim
    place_pose3.position.y = 0.0
    place_pose3.position.z = 0.183676720426 - off
    place_pose3.orientation.x = quat1[0]
    place_pose3.orientation.y = quat1[1]
    place_pose3.orientation.z = quat1[2]
    place_pose3.orientation.w = quat1[3]

    # Place pose 4
    place_pose4 = Pose()
    place_pose4.position.x = 0.659679836383
    place_pose4.position.y = -0.06
    place_pose4.position.z = 0.27 - off
    place_pose4.orientation.x = quat2[0]
    place_pose4.orientation.y = quat2[1]
    place_pose4.orientation.z = quat2[2]
    place_pose4.orientation.w = quat2[3]

    # Place pose 5 (y + 0.065)
    place_pose5 = Pose()
    place_pose5.position.x = 0.659679836383
    place_pose5.position.y = 0.005 - trim
    place_pose5.position.z = 0.27 - off
    place_pose5.orientation.x = quat2[0]
    place_pose5.orientation.y = quat2[1]
    place_pose5.orientation.z = quat2[2]
    place_pose5.orientation.w = quat2[3]

    # Place pose 6
    place_pose6 = Pose()
    place_pose6.position.x = 0.659679836383
    place_pose6.position.y = 0.07 - 2*trim
    place_pose6.position.z = 0.27 - off
    place_pose6.orientation.x = quat2[0]
    place_pose6.orientation.y = quat2[1]
    place_pose6.orientation.z = quat2[2]
    place_pose6.orientation.w = quat2[3]


    # Place pose 7
    place_pose7 = Pose()
    place_pose7.position.x = 0.589679836383
    place_pose7.position.y = 0.0
    place_pose7.position.z = 0.357 - off
    place_pose7.orientation.x = quat1[0]
    place_pose7.orientation.y = quat1[1]
    place_pose7.orientation.z = quat1[2]
    place_pose7.orientation.w = quat1[3]

    # Place pose 8 (x + 0.07)
    place_pose8 = Pose()
    place_pose8.position.x = 0.659679836383 - trim
    place_pose8.position.y = 0.0
    place_pose8.position.z = 0.357 - off
    place_pose8.orientation.x = quat1[0]
    place_pose8.orientation.y = quat1[1]
    place_pose8.orientation.z = quat1[2]
    place_pose8.orientation.w = quat1[3]


    # Place pose 9
    place_pose9 = Pose()
    place_pose9.position.x = 0.729679836383 - 2*trim
    place_pose9.position.y = 0.0
    place_pose9.position.z = 0.357 - off
    place_pose9.orientation.x = quat1[0]
    place_pose9.orientation.y = quat1[1]
    place_pose9.orientation.z = quat1[2]
    place_pose9.orientation.w = quat1[3]

    # Place pose 10
    place_pose10 = Pose()
    place_pose10.position.x = 0.659679836383
    place_pose10.position.y = -0.06
    place_pose10.position.z = 0.444 - off
    place_pose10.orientation.x = quat2[0]
    place_pose10.orientation.y = quat2[1]
    place_pose10.orientation.z = quat2[2]
    place_pose10.orientation.w = quat2[3]

    # Place pose 11 (y + 0.065)
    place_pose11 = Pose()
    place_pose11.position.x = 0.659679836383
    place_pose11.position.y = 0.005 - trim
    place_pose11.position.z = 0.444 - off
    place_pose11.orientation.x = quat2[0]
    place_pose11.orientation.y = quat2[1]
    place_pose11.orientation.z = quat2[2]
    place_pose11.orientation.w = quat2[3]

    # Place pose 12
    place_pose12 = Pose()
    place_pose12.position.x = 0.659679836383
    place_pose12.position.y = 0.07 - 2*trim
    place_pose12.position.z = 0.444 - off
    place_pose12.orientation.x = quat2[0]
    place_pose12.orientation.y = quat2[1]
    place_pose12.orientation.z = quat2[2]
    place_pose12.orientation.w = quat2[3]


    # Spawn table
    spawn_gazebo_table()

    # Spawn brick1
    spawn_gazebo_brick(brick_pose=place_pose1, count=1)

    rospy.sleep(2.0)

    # Spawn brick2
    spawn_gazebo_brick(brick_pose=place_pose2, count=2)

    rospy.sleep(2.0) 

    # Spawn brick3
    spawn_gazebo_brick(brick_pose=place_pose3, count=3)

    rospy.sleep(2.0)

    # Spawn brick4
    spawn_gazebo_brick(brick_pose=place_pose4, count=4)

    rospy.sleep(2.0)

    # Spawn brick5
    spawn_gazebo_brick(brick_pose=place_pose5, count=5)

    rospy.sleep(2.0)

    # Spawn brick6
    spawn_gazebo_brick(brick_pose=place_pose6, count=6)

    rospy.sleep(2.0) 

    # Spawn brick7
    spawn_gazebo_brick(brick_pose=place_pose7, count=7)

    rospy.sleep(2.0)

    # Spawn brick8
    spawn_gazebo_brick(brick_pose=place_pose8, count=8)

    rospy.sleep(2.0)

    # Spawn brick9
    spawn_gazebo_brick(brick_pose=place_pose9, count=9)

    rospy.sleep(2.0)

    # Spawn brick10
    spawn_gazebo_brick(brick_pose=place_pose10, count=10)

    rospy.sleep(2.0) 

    # Spawn brick11
    spawn_gazebo_brick(brick_pose=place_pose11, count=11)

    rospy.sleep(2.0)

    # Spawn brick12
    spawn_gazebo_brick(brick_pose=place_pose12, count=12)

    rospy.sleep(2.0) 



    # Delete all models
    delete_gazebo_models()

    #rospy.on_shutdown(delete_gazebo_models)

    


if __name__ == '__main__':
    sys.exit(main())
    #delete_gazebo_models()
