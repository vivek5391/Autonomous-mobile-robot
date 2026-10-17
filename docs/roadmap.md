# Development Roadmap

## Milestone 1 — Robot description
- [x] Create differential-drive URDF/Xacro model
- [x] Add RViz visualization launch and configuration
- [ ] Pass CI build and expand Xacro successfully

## Milestone 2 — Simulation and motion
- [x] Add Gazebo Sim world and differential-drive plugin configuration
- [x] Add robot-spawn and bridge launch pipeline
- [ ] Confirm robot spawns correctly in Gazebo Harmonic
- [ ] Verify wheel motion with /cmd_vel
- [ ] Test keyboard teleoperation

## Milestone 3 — LiDAR, odometry, and TF
- [x] Add simulated 2D GPU LiDAR model
- [x] Configure /scan, raw odometry, and simulation clock bridges
- [x] Add starter robot_localization EKF configuration
- [ ] Verify /scan, /odom, /clock, and TF in a running simulation

## Milestone 4 — Mapping
- [x] Add starter SLAM Toolbox parameters and launch file
- [ ] Run SLAM with verified sensor data and TF
- [ ] Save and reload a map

## Milestone 5 — Autonomous navigation
- [x] Add a Nav2 launch entry point
- [ ] Configure/tune Nav2 frames, costmaps, footprint, and velocity limits
- [ ] Send goals in RViz
- [ ] Verify obstacle avoidance in simulation

## Milestone 6 — Quality and portfolio
- [x] Add GitHub Actions ROS 2 Jazzy build workflow
- [ ] Get a green CI run and fix all build/Xacro errors
- [ ] Add screenshots or a short simulation demo only after the run is successful
- [ ] Document exact tested OS, ROS, and Gazebo versions

## Working rule

Files and launch entry points are implementation drafts until CI and local simulation checks pass. Never mark simulation, mapping, or navigation as tested based only on committed files. This is a learning/portfolio model, not a validated physical robot.
