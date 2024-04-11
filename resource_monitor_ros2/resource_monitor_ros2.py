import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ResourceMonitor(Node):
    def __init__(self):
        super().__init__('resource_monitor')
        self.cpu_pub = self.create_publisher(Float64, '/resources/cpu', 10)
        self.memory_pub = self.create_publisher(Float64, '/resources/memory', 10)
        self.network_in_pub = self.create_publisher(Float64, '/resources/network_in', 10)
        self.network_out_pub = self.create_publisher(Float64, '/resources/network_out', 10)
        self.timer = self.create_timer(5.0, self.publish_usage)

    def publish_usage(self):
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent

        net_io_counters = psutil.net_io_counters()
        network_in_rate = net_io_counters.bytes_recv / 1024.0  # Convert bytes to KB
        network_out_rate = net_io_counters.bytes_sent / 1024.0  # Convert bytes to KB

        cpu_msg = Float64()
        cpu_msg.data = cpu_usage
        self.cpu_pub.publish(cpu_msg)

        memory_msg = Float64()
        memory_msg.data = memory_usage
        self.memory_pub.publish(memory_msg)

        network_in_msg = Float64()
        network_in_msg.data = network_in_rate
        self.network_in_pub.publish(network_in_msg)

        network_out_msg = Float64()
        network_out_msg.data = network_out_rate
        self.network_out_pub.publish(network_out_msg)

def main(args=None):
    rclpy.init(args=args)
    resource_monitor = ResourceMonitor()
    rclpy.spin(resource_monitor)
    resource_monitor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
