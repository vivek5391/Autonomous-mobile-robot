# Development Roadmap

## Milestone 1 — Robot description
- [x] Create a differential-drive robot Xacro model
- [x] Add a launch file for RViz visualization
- [ ] Build and test on Ubuntu 24.04 + ROS 2 Jazzy

## Milestone 2 — Motion and simulation
- [x] Add a Gazebo Sim differential-drive plugin configuration
- [x] Add an initial Gazebo launch pipeline for robot spawning
- [ ] Build and test the Gazebo spawn pipeline
- [ ] Drive the robot with keyboard teleoperation

## Milestone 3 — Sensors and odometry
- [x] Add a simulated 2D LiDAR model and bridge configuration
- [x] Add initial Gazebo-to-ROS bridge configuration for odometry
- [ ] Verify /scan, /odom, and TF topics in a running simulation

## Milestone 4 — Mapping
- [x] Add starter SLAM Toolbox parameters and launch file
- [ ] Run SLAM Toolbox with a verified live /scan and odometry/TF
- [ ] Save and reload a map

## Milestone 5 — Autonomous navigation
- [ ] Configure Nav2
- [ ] Send navigation goals in RViz
- [ ] Tune costmaps and verify obstacle avoidance

## Working rule

Only mark a feature complete after it has been run and checked. The current simulation, sensor, and SLAM files are implementation drafts until tested on Ubuntu 24.04 + ROS 2 Jazzy + Gazebo Sim Harmonic. This is a simulation learning model, not a validated physical robot design.
