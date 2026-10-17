from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    package_share = FindPackageShare('mobile_robot_description')
    default_world = PathJoinSubstitution([
        package_share, 'worlds', 'empty.world.sdf'
    ])
    xacro_file = PathJoinSubstitution([
        package_share, 'urdf', 'mobile_robot.urdf.xacro'
    ])
    bridge_config = PathJoinSubstitution([
        package_share, 'config', 'ros_gz_bridge.yaml'
    ])
    ekf_config = PathJoinSubstitution([
        package_share, 'config', 'ekf.yaml'
    ])
    robot_description = Command(['xacro', ' ', xacro_file])

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=default_world,
            description='Path to the Gazebo Sim world SDF file',
        ),
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', LaunchConfiguration('world')],
            output='screen',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description,
                'use_sim_time': True,
            }],
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='ros_gz_bridge',
            output='screen',
            parameters=[{'config_file': bridge_config}],
        ),
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config, {'use_sim_time': True}],
            remappings=[('/odometry/filtered', '/odom')],
        ),
        # Give Gazebo a moment to start before spawning the robot.
        TimerAction(
            period=3.0,
            actions=[
                Node(
                    package='ros_gz_sim',
                    executable='create',
                    name='spawn_mobile_robot',
                    output='screen',
                    arguments=[
                        '-name', 'mobile_robot',
                        '-topic', 'robot_description',
                        '-z', '0.0',
                    ],
                )
            ],
        ),
    ])
