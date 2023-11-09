#!/usr/opt/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class number_counter(Node):
    count = 0
    
    def __init__(self):
        super().__init__("number_counter")
        self.get_logger().info("Number Counter Node has been started")
        self.subscriber_ = self.create_subscription(Int64, "number", self.callbackSubcriber, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
    
    def callbackSubcriber(self, msg):
        #self.get_logger().info("Msg Subscribed " + str(msg.data))
        self.count += msg.data
        msg = Int64()
        msg.data = self.count
        self.publishMsg(msg)
    
    def publishMsg(self, msg):
        self.publisher_.publish(msg)
        self.get_logger().info("Msg Published " + str(msg.data))
        
def main():
    rclpy.init(args=None)
    node = number_counter()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__name__":
    main()
    