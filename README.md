# Autonomous Mobile Robot — ROS 2

A simulation-first differential-drive autonomous mobile robot portfolio project. The aim is to build a complete ROS 2 workflow: robot description, Gazebo simulation, teleoperation, LiDAR, odometry/TF, mapping, and autonomous navigation.

## Tech stack

- Ubuntu 24.04 · ROS 2 Jazzy · Gazebo Sim Harmonic
- URDF/Xacro · RViz2 · ros_gz_sim / ros_gz_bridge
- Simulated 2D GPU LiDAR · robot_localization
- SLAM Toolbox · Nav2 · GitHub Actions CI

## Current status

**In development; local build and simulation validation are pending.** Repository files have been created and checked through GitHub, but the robot has not yet been launched on a local ROS 2 + Gazebo installation. Treat launch and sensor integration as unverified until the CI build and simulation checks pass.

## 1. Install dependencies

On Ubuntu 24.04 with ROS 2 Jazzy configured:

\`\`\`bash
sudo apt update
sudo apt install \
  ros-jazzy-xacro \
  ros-jazzy-robot-state-publisher \
  ros-jazzy-joint-state-publisher-gui \
  ros-jazzy-rviz2 \
  ros-jazzy-ros-gz-sim \
  ros-jazzy-ros-gz-bridge \
  ros-jazzy-robot-localization \
  ros-jazzy-slam-toolbox \
  ros-jazzy-nav2-bringup \
  ros-jazzy-teleop-twist-keyboard
\`\`\`

## 2. Clone and build

\`\`\`bash
mkdir -p ~/amr_ws/src
cd ~/amr_ws/src
git clone https://github.com/vivek5391/Autonomous-mobile-robot.git
cd ~/amr_ws
source /opt/ros/jazzy/setup.bash
rosdep install --from-paths src --ignore-src -r -y --rosdistro jazzy
colcon build --symlink-install
source install/setup.bash
\`\`\`

## 3. View the robot model in RViz

\`\`\`bash
ros2 launch mobile_robot_description display.launch.py
\`\`\`

If the model is missing, check the RViz Fixed Frame (base_footprint) and the RobotModel display.

## 4. Start Gazebo simulation

\`\`\`bash
ros2 launch mobile_robot_description gazebo_world.launch.py
\`\`\`

Check topics in another terminal:

\`\`\`bash
source /opt/ros/jazzy/setup.bash
source ~/amr_ws/install/setup.bash
ros2 topic list
ros2 topic echo /scan --once
ros2 topic echo /odom --once
\`\`\`

## 5. Teleoperate (after confirming /cmd_vel and wheel motion)

\`\`\`bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
\`\`\`

If keyboard teleop publishes a different velocity topic, remap it to /cmd_vel.

## 6. Start SLAM mapping (after /scan, /odom, and TF are verified)

\`\`\`bash
ros2 launch mobile_robot_description slam.launch.py
\`\`\`

Save a map from a separate terminal:

\`\`\`bash
ros2 run nav2_map_server map_saver_cli -f ~/amr_map
\`\`\`

## 7. Start Nav2 (after a map exists and frame/topic configuration is checked)

\`\`\`bash
ros2 launch mobile_robot_description navigation.launch.py
\`\`\`

This launch entry point uses Nav2's standard parameter file as a starter. For reliable autonomous navigation, the costmaps, footprint, scan topic, frames, controller limits, and map/SLAM integration must be reviewed and tuned for this robot before use.

## Repository structure

\`\`\`text
src/mobile_robot_description/
├── config/       # bridge, EKF, SLAM parameters
├── launch/       # RViz, Gazebo, SLAM and Nav2 entry points
├── rviz/         # RViz configuration
├── urdf/         # robot model and sensor configuration
└── worlds/       # Gazebo world
docs/             # roadmap and validation instructions
.github/workflows # ROS 2 CI workflow
\`\`\`

## Milestones

1. Robot model and RViz visualization
2. Gazebo spawn, drive control, and topic validation
3. LiDAR, odometry, and TF validation
4. SLAM mapping and map saving
5. Nav2 goal navigation and obstacle avoidance

See [roadmap](docs/roadmap.md) and [simulation validation guide](docs/gazebo-simulation.md).

## Engineering honesty

The model and sensor are simulated and are not a validated hardware design. A feature is not considered complete until it has been built, run, and checked.
