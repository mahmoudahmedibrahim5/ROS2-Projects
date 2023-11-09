#!/usr/opt/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_publisher(Node):
    constNumber = 2
    
    def __init__(self):
        super().__init__("number_publisher")
        self.get_logger().info("Number Publisher Node has been started")
        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(0.5, self.callbackTimer)
    
    def callbackTimer(self):
        msg = Int64()
        msg.data = self.constNumber
        self.publishMsg(msg)
    
    def publishMsg(self, msg):
        self.publisher_.publish(msg)
        self.get_logger().info("Msg Published")
        
def main():
    rclpy.init(args=None)
    node = number_publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
