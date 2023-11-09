#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class controller(Node):
    def __init__(self):
        super().__init__("controller")
        self.get_logger().info("Controller Node has been started")
        self.subscriber_ = self.create_subscription(String, "Hello", self.callbackSubscribe, 10)
    
    def callbackSubscribe(self, msg):
        self.get_logger().info(msg.data)
        

def main():
    rclpy.init()
    node = controller()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
