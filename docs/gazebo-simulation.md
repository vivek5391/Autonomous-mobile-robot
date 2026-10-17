# Gazebo Simulation — Preparation

This repository includes a minimal Gazebo Sim world and a launch file to open it.

## Current status

The empty world is only a starting point. The robot is **not yet spawned into Gazebo**. Differential-drive control, LiDAR, and ROS 2 bridge topics are not configured. These need a compatible Gazebo Sim release and matching ROS 2 integration packages.

## Next steps

1. Confirm the installed ROS 2 and Gazebo versions on the laptop.
2. Launch the empty world.
3. Add the robot spawn pipeline using the matching Gazebo integration.
4. Configure differential-drive control and command topics.
5. Add a 2D LiDAR sensor and bridge its scan topic to ROS 2.
6. Test teleoperation before beginning SLAM and Nav2.

## Launch command after building

    ros2 launch mobile_robot_description gazebo_world.launch.py

This requires Gazebo Sim (the gz sim command) to be installed and available in the terminal. The files have been committed but have not yet been tested on the user's laptop.
