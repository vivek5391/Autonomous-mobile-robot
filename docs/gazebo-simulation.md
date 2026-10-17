# Gazebo Simulation — Implementation in Progress

## What is now configured in the repository

- Gazebo Sim world launch.
- A differential-drive plugin in the robot Xacro.
- A 2D GPU LiDAR model publishing the Gazebo `/scan` topic.
- A launch pipeline intended to publish `robot_description`, spawn the robot, and start `ros_gz_bridge`.
- Bridge configuration for `/cmd_vel`, `/odom`, and `/scan`.

## Important test status

These files were edited through GitHub and have **not been built or run locally yet**. Treat this as implementation in progress, not a verified working simulation. Gazebo Sim Harmonic and the matching ROS 2 Jazzy integration packages must be installed.

## Build and launch on Ubuntu 24.04 + ROS 2 Jazzy

Install the packages:

    sudo apt update
    sudo apt install ros-jazzy-xacro ros-jazzy-robot-state-publisher ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge

Build from the workspace root:

    source /opt/ros/jazzy/setup.bash
    colcon build --symlink-install
    source install/setup.bash

Launch:

    ros2 launch mobile_robot_description gazebo_world.launch.py

In a second terminal, inspect topics:

    source /opt/ros/jazzy/setup.bash
    source install/setup.bash
    ros2 topic list
    ros2 topic echo /scan --once

If the robot does not appear or the scan topic is missing, capture the terminal error output before changing plugin or bridge settings.

## Next validation checks

1. Confirm the robot spawns in Gazebo.
2. Confirm `/scan` produces LaserScan messages.
3. Confirm `/odom` produces odometry messages.
4. Send a very small velocity command and verify wheel motion.
5. Only after these pass, add teleoperation and SLAM Toolbox.

The LiDAR is a simulated sensor; it is not a hardware specification.
