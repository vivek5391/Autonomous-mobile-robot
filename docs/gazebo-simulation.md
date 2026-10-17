# Simulation, LiDAR, SLAM, and Nav2 Validation

## Target environment

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Sim Harmonic

## Status

The repository now contains a Gazebo world, a robot-spawn launch pipeline, a simulated 2D GPU LiDAR, bridge configuration, an EKF configuration, a SLAM Toolbox launch entry point, and a Nav2 launch entry point. These have been edited through GitHub but **have not been run locally yet**.

## Build

Install the dependencies listed in the main README, then run:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/amr_ws
rosdep install --from-paths src --ignore-src -r -y --rosdistro jazzy
colcon build --symlink-install
source install/setup.bash
```

## Validation order

1. Start Gazebo:

   ```bash
   ros2 launch mobile_robot_description gazebo_world.launch.py
   ```

2. Check the basic topics in another sourced terminal:

   ```bash
   ros2 topic list
   ros2 topic echo /clock --once
   ros2 topic echo /scan --once
   ros2 topic echo /odom/raw --once
   ros2 topic echo /odom --once
   ```

3. Confirm TF is connected:

   ```bash
   ros2 run tf2_tools view_frames
   ```

4. Send a low-speed command only after confirming the robot has spawned:

   ```bash
   ros2 topic pub --rate 2 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.05}, angular: {z: 0.0}}"
   ```

   Stop publishing with Ctrl+C. Confirm the robot actually moves in Gazebo.

5. Test keyboard control:

   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```

6. Start SLAM only after sensor, odometry, and TF checks pass:

   ```bash
   ros2 launch mobile_robot_description slam.launch.py
   ```

7. Save a map after it has visibly updated:

   ```bash
   ros2 run nav2_map_server map_saver_cli -f ~/amr_map
   ```

8. Review Nav2 parameters and the map/SLAM integration before starting navigation:

   ```bash
   ros2 launch mobile_robot_description navigation.launch.py
   ```

## Common failure checks

- If the robot fails to spawn, inspect the Gazebo and ros_gz_sim create terminal output.
- If /scan is absent, inspect the Gazebo sensor and bridge logs.
- If /odom is absent, check /odom/raw and the EKF node.
- If SLAM reports transform errors, inspect the map, odom, base_footprint, and lidar_link transform chain.
- Do not claim autonomous navigation works until a map, TF, localization, and controller behavior have all been checked.

The LiDAR and robot are simulated; this is not a validated physical robot design.
