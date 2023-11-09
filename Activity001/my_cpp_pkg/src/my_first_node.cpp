#include "rclcpp/rclcpp.hpp"

class MyNode: public rclcpp::Node
{
private:
    void timerCallBack(void){
        counter++;
        RCLCPP_INFO(this->get_logger(), "Hello %d", counter);
    }
    rclcpp::TimerBase::SharedPtr timer;
public:
    int counter;
    MyNode():Node("CPP_Test"){
        counter = 0;
        RCLCPP_INFO(this->get_logger(), "Hello ROS2 with CPP");
    }

    void printHello(void){
        timer = this->create_wall_timer(std::chrono::milliseconds(500) , std::bind(&MyNode::timerCallBack, this));
    }
};



int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyNode>();
    node->printHello();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
