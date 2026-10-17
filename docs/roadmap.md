# Development Roadmap

## Milestone 1 — Robot description
- [x] Create a differential-drive robot Xacro model
- [x] Add a launch file for RViz visualization
- [ ] Build and test on Ubuntu 24.04 + ROS 2 Jazzy

## Milestone 2 — Motion and simulation
- [ ] Add ros2_control or a simulation drive plugin
- [ ] Add Gazebo simulation world and spawn launch file
- [ ] Drive the robot with keyboard teleoperation

## Milestone 3 — Sensors and odometry
- [ ] Add a 2D LiDAR model and scan topic
- [ ] Add wheel odometry and TF frames
- [ ] Verify the TF tree and sensor data

## Milestone 4 — Mapping
- [ ] Configure SLAM Toolbox
- [ ] Save and reload a map

## Milestone 5 — Autonomous navigation
- [ ] Configure Nav2
- [ ] Send navigation goals in RViz
- [ ] Tune costmaps and verify obstacle avoidance

## Working rule

Only mark a feature complete after it has been run and checked. The initial model is a learning/simulation model, not a validated physical robot design.
