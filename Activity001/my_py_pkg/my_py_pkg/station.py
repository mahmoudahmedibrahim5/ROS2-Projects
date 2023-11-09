#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import time

class Station(Node):
    def __init__(self):
        super().__init__("station")
        self.get_logger().info("Station Node has been started")
        self.publisher_ = self.create_publisher(String, "Hello", 10)
    
    def publish(self, msg):
        self.get_logger().info("Message Published")
        self.publisher_.publish(msg)

def main():
    rclpy.init(args=None)
    node = Station()
    message = String()
    message.data = "Hello controller"
    for i in range(6):
        #time.sleep(1)
        node.publish(message)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
    