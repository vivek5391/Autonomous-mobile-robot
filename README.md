# Autonomous Mobile Robot (ROS 2)

A simulation-first differential-drive autonomous mobile robot project built with ROS 2. The goal is to develop the robot step by step, from a clean robot model to mapping and autonomous navigation.

## Planned features

- Differential-drive robot model using URDF/Xacro
- Robot visualization in RViz
- Gazebo Sim world and initial robot-spawn pipeline
- Simulated 2D LiDAR with ROS 2 scan bridge configuration
- Wheel odometry bridge configuration
- SLAM Toolbox mapping preparation
- Keyboard teleoperation and Nav2 (planned)

## Target environment

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Sim Harmonic
- No physical hardware is required for the initial milestones

## Build the workspace

```bash
sudo apt update
sudo apt install ros-jazzy-xacro ros-jazzy-robot-state-publisher ros-jazzy-joint-state-publisher-gui ros-jazzy-rviz2 ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge ros-jazzy-slam-toolbox
mkdir -p ~/amr_ws/src
cd ~/amr_ws/src
git clone https://github.com/vivek5391/Autonomous-mobile-robot.git
cd ~/amr_ws
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## View the robot in RViz

```bash
ros2 launch mobile_robot_description display.launch.py
```

If RViz opens without the model, check that the Fixed Frame is `base_footprint` and add a **RobotModel** display.

## Start the simulation

```bash
ros2 launch mobile_robot_description gazebo_world.launch.py
```

The launch file is intended to start Gazebo, publish the robot description, spawn the robot, and bridge `/cmd_vel`, `/odom`, and `/scan`. These steps still need to be verified on a machine with the target ROS/Gazebo installation.

## SLAM preparation

A starter SLAM Toolbox configuration and launch file are included. After the simulation is verified and `/scan`, `/odom`, and TF are confirmed, start mapping with:

```bash
ros2 launch mobile_robot_description slam.launch.py
```

Save a map only after confirming that the robot moves correctly and the map updates consistently.

## Project status

**Implementation in progress — not yet locally tested.** Files are being developed through GitHub because local ROS 2/Gazebo execution is not currently available. No feature is described as working until it has been built and tested.

See [docs/gazebo-simulation.md](docs/gazebo-simulation.md) and [docs/roadmap.md](docs/roadmap.md).
