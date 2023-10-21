import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self,data):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.data = data

    def listener_callback(self, msg):
        if len(self.data) > 10:
            self.get_logger().info(f'Collected data: {self.data}')
            self.destroy_node()
            return
        self.data.append(msg.data)


def main(args=None):
    rclpy.init(args=args)
    data=list()
    minimal_subscriber = MinimalSubscriber(data)

    rclpy.spin(minimal_subscriber)
  

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    #minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
