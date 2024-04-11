import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='resource_monitor_ros2',
            executable='resource_monitor',
            name='resource_monitor',
            output='screen',
        ),
        # Add other monitoring nodes here if needed
    ])
