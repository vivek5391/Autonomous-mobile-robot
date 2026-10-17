# Gazebo Simulation and SLAM — Implementation in Progress

## Configured in the repository

- Gazebo Sim world launch.
- Differential-drive plugin configuration in the robot Xacro.
- A simulated 2D GPU LiDAR intended to publish `/scan`.
- Initial launch pipeline to publish `robot_description`, spawn the robot, and start `ros_gz_bridge`.
- Bridge configuration for `/cmd_vel`, `/odom`, and `/scan`.
- Starter SLAM Toolbox mapping parameters and a `slam.launch.py` launch file.

## Important test status

These files were edited through GitHub and have **not been built or run locally**. Treat them as implementation drafts, not a verified working simulation. The target environment is Ubuntu 24.04, ROS 2 Jazzy, and Gazebo Sim Harmonic.

## Install and build

    sudo apt update
    sudo apt install ros-jazzy-xacro ros-jazzy-robot-state-publisher ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge ros-jazzy-slam-toolbox
    source /opt/ros/jazzy/setup.bash
    cd ~/amr_ws
    colcon build --symlink-install
    source install/setup.bash

## Start Gazebo

    ros2 launch mobile_robot_description gazebo_world.launch.py

Check the topics in a second terminal:

    source /opt/ros/jazzy/setup.bash
    source ~/amr_ws/install/setup.bash
    ros2 topic list
    ros2 topic echo /scan --once
    ros2 topic echo /odom --once

## Start mapping — only after simulation checks pass

In another terminal:

    source /opt/ros/jazzy/setup.bash
    source ~/amr_ws/install/setup.bash
    ros2 launch mobile_robot_description slam.launch.py

SLAM needs a valid scan stream and a correct transform chain between `map`, `odom`, and `base_footprint`. If the robot does not spawn, the topics are absent, or the transform chain is broken, SLAM will not work yet; save the terminal errors for debugging.

## Validation checklist

1. Confirm the robot appears in Gazebo.
2. Confirm `/scan` produces LaserScan messages.
3. Confirm `/odom` produces odometry messages.
4. Confirm the TF tree is connected.
5. Send a small velocity command and verify the robot moves.
6. Only then test SLAM mapping and map saving.

The LiDAR is simulated and is not a hardware specification. No feature is marked tested until it has been run.
