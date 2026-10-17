# Autonomous Mobile Robot (ROS 2)

A simulation-first differential-drive autonomous mobile robot project built with ROS 2. The goal is to develop the robot step by step, from a clean URDF model to mapping and autonomous navigation.

## Planned features

- Differential-drive robot model using URDF/Xacro
- Robot visualization in RViz
- Gazebo simulation
- Keyboard teleoperation
- LiDAR and wheel odometry
- SLAM Toolbox mapping
- Nav2 autonomous navigation

## Target environment

- Ubuntu 24.04
- ROS 2 Jazzy
- Laptop-based simulation; physical hardware is not required for the initial milestones

## Current milestone: robot description

Install the required tools:

```bash
sudo apt update
sudo apt install ros-jazzy-xacro ros-jazzy-robot-state-publisher ros-jazzy-joint-state-publisher-gui ros-jazzy-rviz2
```

Create a workspace and clone this repository:

```bash
git clone https://github.com/vivek5391/Autonomous-mobile-robot.git ~/amr_ws
cd ~/amr_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch mobile_robot_description display.launch.py
```

If RViz opens without the model, check that the Fixed Frame is `base_footprint` and add a **RobotModel** display.

## Project status

The first milestone is a basic robot description and RViz visualization. Gazebo, sensors, SLAM, and Nav2 will be added in later milestones. Features are not considered complete until they are implemented and tested.

## Gazebo preparation

A minimal Gazebo Sim world and launch file are included as preparation. The robot is not yet spawned into the world, and drive control/LiDAR are still future work. See [docs/gazebo-simulation.md](docs/gazebo-simulation.md) for current status and next steps.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).
