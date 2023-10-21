# Turtlesim installation

### First of all, make sure your system is up-to-date
```
sudo apt update
```
### Install the turtlesim library
```
ulugbekmirzabakhromov@ubuntu:~$ sudo apt install ros-rolling-turtlesim
Reading package lists... Done
Building dependency tree       
Reading state information... Done
....
```
### Check that the package is installed
```
ulugbekmirzabakhromov@ubuntu:~$ ros2 pkg executables turtlesim
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```
### To start turtlesim, enter the following command in your terminal
```
ulugbekmirzabakhromov@ubuntu:~$ ros2 run turtlesim turtlesim_node
[INFO] [1663638092.636082943] [turtlesim]: Starting turtlesim with node name /turtlesim
[INFO] [1663638092.645975073] [turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-09-21%20at%2014.03.15.png)
### To control the turtle type the following command:
```
ulugbekmirzabakhromov@ubuntu:~$ ros2 run turtlesim turtle_teleop_key
Reading from keyboard
---------------------------
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
'Q' to quit.
```
### RQT: installation
```bash
#  MAKE SURE YOUR SYSTEM IS UP-TO-DATE
ulugbekmirzabakhromov@ubuntu:~$ sudo apt update

# INSTALL THE RQT LIBRARY AND ITS PLUGINS
ulugbekmirzabakhromov@ubuntu:~$ sudo apt install ~nros-rolling-rqt*
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  pybind11-dev ros-rolling-class-loader
  ...
# To run rqt by just typing command "rqt"
ulugbekmirzabakhromov@ubuntu:~$ rqt
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-09-21%20at%2018.40.15.png)
# RQT: running rqt_console
```
ulugbekmirzabakhromov@ubuntu:~$ ros2 run rqt_console rqt_console
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-09-21%20at%2021.45.00.png)
### Turtlesim simulation
```bash
# RUN THE TURTLESIM_NODE IN A NEW TAB
ulugbekmirzabakhromov@ubuntu:~$ ros2 run turtlesim turtlesim_node
[INFO] [1664067181.891114659] [turtlesim]: Starting turtlesim with node name /turtlesim
[INFO] [1664067181.940055496] [turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
# RUN THE TURTLE_TELEOP_KEY TO MOVE THE TURTLE IN A NEW TAB
ulugbekmirzabakhromov@ubuntu:~$ ros2 run turtlesim turtle_teleop_key
Reading from keyboard
---------------------------
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
'Q' to quit.
#RUN THE rqt in your terminal
ulugbekmirzabakhromov@ubuntu:~$ rqt
#CHANGE THE /SPAWN SERVICE PARAMETERS TO RUN TURTLE2
#TO RUN THE TURTLE TO RUN THIS COMMAND
ulugbekmirzabakhromov@ubuntu:~$ ros2 run turtlesim turtle_teleop_key --ros-args --remap turtle1/cmd_vel:=turtle2/cmd_vel
Reading from keyboard
---------------------------
Use arrow keys to move the turtle.
Use G|B|V|C|D|E|R|T keys to rotate to absolute orientations. 'F' to cancel a rotation.
'Q' to quit.
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-09-25%20at%2010.11.58.png)
# TURTLE simulation
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Peek%202022-09-24%2018-24.gif)
### ROS2 Colcon
```bash
# INSTALLING Colcon
ulugbekmirzabakhromov@ubuntu:~$ sudo apt install python3-colcon-common-extensions
[sudo] password for ulugbekmirzabakhromov: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3-colcon-common-extensions is already the newest version (0.3.0-1).
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.

-----------------------------------
 # ROS2 Colcon: Create a workspace
 ----------------------------------
ulugbekmirzabakhromov@ubuntu:~$ echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
ulugbekmirzabakhromov@ubuntu:~$ echo "export _colcon_cd_root=/opt/ros/rolling/" >> ~/.bashrc
ulugbekmirzabakhromov@ubuntu:~$ source /opt/ros/rolling/setup.bash
ulugbekmirzabakhromov@ubuntu:~$ mkdir -p ~/ros2_ws/src
ulugbekmirzabakhromov@ubuntu:~$ cd ~/ros2_ws
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ git clone https://github.com/ros/ros_tutorials.git -b rolling-devel
Cloning into 'ros_tutorials'...
remote: Enumerating objects: 2841, done.
remote: Counting objects: 100% (161/161), done.
remote: Compressing objects: 100% (88/88), done.
remote: Total 2841 (delta 93), reused 131 (delta 71), pack-reused 2680
Receiving objects: 100% (2841/2841), 617.66 KiB | 7.72 MiB/s, done.
Resolving deltas: 100% (1710/1710), done.
# RESOLVE DEPENDENCIES
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ rosdep install -i --from-path src --rosdistro rolling -y
All required rosdeps installed successfully

# BUILD THE WORKSPACE WITH Colcon
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ colcon build
[1.070s] WARNING:colcon.colcon_core.package_selection:Some selected packages are already built in one or more underlay workspaces:
	'turtlesim' is in: /opt/ros/rolling, /opt/ros/foxy
If a package in a merged underlay workspace is overridden and i
...
This may be promoted to an error in a future release of colcon-override-check.
Starting >>> turtlesim
[Processing: turtlesim]                             
[Processing: turtlesim] 
....
# SOURCE THE OVERLAY
ulugbekmirzabakhromov@ubuntu:~$ source /opt/ros/rolling/setup.bash
ulugbekmirzabakhromov@ubuntu:~$ cd ~/ros2_ws
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ . install/local_setup.bash
# MODIFY THE OVERLAY
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ cd src
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ ls
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ git clone https://github.com/ros/ros_tutorials
Cloning into 'ros_tutorials'...
remote: Enumerating objects: 2841, done.
remote: Counting objects: 100% (161/161), done.
remote: Compressing objects: 100% (88/88), done.
remote: Total 2841 (delta 93), reused 131 (delta 71), pack-reused 2680
Receiving objects: 100% (2841/2841), 617.66 KiB | 855.00 KiB/s, done.
Resolving deltas: 100% (1710/1710), done.
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ ls
ros_tutorials
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ cd ros_tutorials
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/ros_tutorials$ ls
roscpp_tutorials  rospy_tutorials  ros_tutorials  turtlesim
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/ros_tutorials$ cd turtlesim/src
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/ros_tutorials/turtlesim/src$ ls
turtle.cpp  turtle_frame.cpp  turtlesim  turtlesim.cpp
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/ros_tutorials/turtlesim/src$ nano turtle_frame.cpp
```
# Create a package
```bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ ros2 pkg create --build-type ament_python --node-name my_node my_package
going to create a new package
package name: my_package
destination directory: /home/ulugbekmirzabakhromov/ros2_ws/src
package format: 3
version: 0.0.0
...
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ cd ..

# BUILDING PACKAGES
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ colcon build            
Summary: 3 packages finished [4.08s]
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ colcon build --packages-select my_package
Starting >>> my_package
Finished <<< my_package [1.14s]          
Summary: 1 package finished [1.37s]

#SOURCE THE SETUP FILE
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ . install/setup.bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ ros2 run my_package my_node
Hi from my_package.
```

# Writing a publisher and subscriber(Python)
```bash
#MAKE SURE YOU ARE IN THE src FOLDER AND ENTER THE COMMAND FOR CREATING THE PY_PACKAGE
ulugbekmirzabakhromov@ubuntu:~$ cd ~/ros2_ws
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ ros2 pkg create --build-type ament_python py_pubsub
going to create a new package
package name: py_pubsub
destination directory: /home/ulugbekmirzabakhromov/ros2_ws/src
package format: 3
version: 0.0.0
...
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ ls
my_package  my_pkg  py_pubsub  ros_tutorials
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ wget https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
--2022-09-27 21:42:13--  https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
...
2022-09-27 21:42:14 (11.5 MB/s) - ‘publisher_member_function.py’ saved [1576/1576]

#DOWNLOAD THE publisher_member_function.py TO ros2_ws/src/py_pubsub/py_pubsub DIRECTORY

ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/py_pubsub/py_pubsub$ wget https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
--2022-09-27 22:19:36--  https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
...
2022-09-27 22:19:37 (31.7 MB/s) - ‘publisher_member_function.py’ saved [1576/1576]

#ALSO DOWNLOAD THE subscriber_member_function.py 
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/py_pubsub/py_pubsub$ wget https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py
...
2022-09-27 21:54:36 (18.1 MB/s) - ‘subscriber_member_function.py’ saved [1469/1469]
```
# Build and run
```bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ rosdep install -i --from-path src --rosdistro foxy -y
#All required rosdeps installed successfully
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ colcon build --packages-select py_pubsub
Starting >>> py_pubsub
Finished <<< py_pubsub [2.89s]          

Summary: 1 package finished [4.10s]
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ rosdep install -i --from-path src --rosdistro foxy -y
#All required rosdeps installed successfully
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ colcon build --packages-select py_pubsub
Starting >>> py_pubsub
Finished <<< py_pubsub [1.41s]          

Summary: 1 package finished [1.66s]

---------------------------------------
# TESTING THE NODES
---------------------------------------
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ . install/setup.bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ ros2 run py_pubsub talker
[INFO] [1664342591.577268871] [minimal_publisher]: Publishing: "Hello World: 0"
[INFO] [1664342592.061454408] [minimal_publisher]: Publishing: "Hello World: 1"
[INFO] [1664342592.562140724] [minimal_publisher]: Publishing: "Hello World: 2"
[INFO] [1664342593.062828040] [minimal_publisher]: Publishing: "Hello World: 3"
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ . install/setup.bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ ros2 run py_pubsub talker
[INFO] [1664342591.577268871] [minimal_publisher]: Publishing: "Hello World: 0"
[INFO] [1664342592.061454408] [minimal_publisher]: Publishing: "Hello World: 1"
[INFO] [1664342592.562140724] [minimal_publisher]: Publishing: "Hello World: 2"
[INFO] [1664342593.062828040] [minimal_publisher]: Publishing: "Hello World: 3"
```
# Writing a simple service and client(Python)
```bash

#Firstly, create the package into the ros2_ws/src directory
------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ cd ros2_ws
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ cd src
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src$ ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces
going to create a new package
package name: py_srvcli
....

# Write the service node inside the ros2_ws/src/py_srvcli/py_srvcli directory:
------------------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/py_srvcli$ nano service_member_function.py
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/py_srvcli$ nano client_member_function.py

# Add an entry points into the setup.py to be able to run the servic&client nodes.
----------------------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~/ros2_ws/src/py_srvcli$ nano setup.py
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-10-04%20at%2011.20.46.png)
```bash
# BUILD AND RUN
----------------
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ rosdep install -i --from-path src --rosdistro foxy -y
#All required rosdeps installed successfully
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ colcon build --packages-select py_srvcli
Starting >>> py_srvcli
Finished <<< py_srvcli [2.13s]          
Summary: 1 package finished [2.48s]

# Open a new terminal, navigate to ros2_ws, and source the setup files
----------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ . install/setup.bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ ros2 run py_srvcli service
[INFO] [1664849371.615817085] [minimal_service]: Incoming request
a: 2 b: 3
# Do the same thing for the client node
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ . install/setup.bash
ulugbekmirzabakhromov@ubuntu:~/ros2_ws$ ros2 run py_srvcli client 2 3
[INFO] [1664849371.665846561] [minimal_client_async]: Result of add_two_ints: for 2 + 3 = 5
```
#Writing an action server and client(Python)
```bash
#Writing an action server
-------------------------
ulugbekmirzabakhromov@ubuntu:~$ nano fibonacci_action_server.py

#You can get the action_server code from this link:
---------------------------------------------------
```
(https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/action(server%26client)/fibonacci_action_server.py)

```bash
#Run the action server
ulugbekmirzabakhromov@ubuntu:~$ python3 fibonacci_action_server.py 
[INFO] [1664948740.009765307] [fibonacci_action_server]: Executing goal...
[WARN] [1664948740.010891932] [fibonacci_action_server]: Goal state not set, assuming aborted. Goal ID: [ 43 132  59 102 136 104  68 222 136  35 140  96 233 172 179 145]

#In another terminal, use the command line interface to send a goal:
--------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"
Waiting for an action server to become available...
Sending goal:
     order: 5

Goal accepted with ID: 15197cd7683f45baa7c2facdddd31a74

Result:
    sequence:
- 0
- 1
- 1
- 2
- 3
- 5

Goal finished with status: SUCCEEDED

# Writing a action_client server
-------------------------
ulugbekmirzabakhromov@ubuntu:~$ nano fibonacci_action_client.py

#You can get the action_client code from this link:
---------------------------------------------------
```
(https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/action(server%26client)/fibonacci_action_client.py)

```bash
#Run the action client
-----------------------
ulugbekmirzabakhromov@ubuntu:~$ python3 fibonacci_action_client.py
[INFO] [1664949683.787442150] [fibonacci_action_client]: Goal accepted :)
[INFO] [1664949683.790887484] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1])
[INFO] [1664949684.794285170] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2])
[INFO] [1664949685.796666631] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3])
[INFO] [1664949686.799187578] [fibonacci_action_client]: Received feedback: array('i', [0, 1, 1, 2, 3, 5])
....

#In another terminal, run the action_server:
--------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ python3 fibonacci_action_server.py 
[INFO] [1664949683.788839423] [fibonacci_action_server]: Executing goal...
[INFO] [1664949683.789502547] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1])
[INFO] [1664949684.792395799] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2])
[INFO] [1664949685.794762732] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3])
[INFO] [1664949686.797654565] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5])
....
```
#Composing multiple nodes in a single process
```bash
#Discover available components
-------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 component types
robot_state_publisher
  robot_state_publisher::RobotStatePublisher
demo_nodes_cpp
  demo_nodes_cpp::OneOffTimerNode
  ...
  composition::Talker
  composition::Listener
  composition::NodeLikeListener
  composition::Server
  composition::Client
...
```
##Run-time composition using ROS services with a publisher and subscriber
```bash
#In the first shell, start the component container:
---------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 run rclcpp_components component_container

#Open the second shell, start the component container:
------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 component list
/ComponentManager
#Load the talker component(2nd shell)
ulugbekmirzabakhromov@ubuntu:~$ ros2 component load /ComponentManager composition composition::Talker
Loaded component 1 into '/ComponentManager' container node as '/talker'
ulugbekmirzabakhromov@ubuntu:~$ ros2 component load /ComponentManager  composition composition::Listener 
Loaded component 2 into '/ComponentManager' container node as '/listener'

#Now the first shell should show a message that the component was loaded as well as repeated message for publishing a message
-------------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 run rclcpp_components component_container
[INFO] [1665550113.843732655] [ComponentManager]: Load Library: /opt/ros/foxy/lib/libtalker_component.so
[INFO] [1665550113.862136888] [ComponentManager]: Found class: rclcpp_components::NodeFactoryTemplate<composition::Talker>
[INFO] [1665550113.862237852] [ComponentManager]: Instantiate class: rclcpp_components::NodeFactoryTemplate<composition::Talker>
[INFO] [1665550114.878167506] [talker]: Publishing: 'Hello World: 1'
[INFO] [1665550115.878149761] [talker]: Publishing: 'Hello World: 2'
[INFO] [1665550116.877940399] [talker]: Publishing: 'Hello World: 3'
[INFO] [1665550117.877841432] [talker]: Publishing: 'Hello World: 4'
[INFO] [1665550118.877683620] [talker]: Publishing: 'Hello World: 5'
[INFO] [1665550119.877550575] [talker]: Publishing: 'Hello World: 6'
.....

#Run another command in the second shell to load the listener component
-----------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 component load /ComponentManager  composition composition::Listener 
Loaded component 2 into '/ComponentManager' container node as '/listener'

#Now the first shell should show repeated output for each received message
---------------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ ros2 run rclcpp_components component_container
[INFO] [1665550184.794836985] [ComponentManager]: Load Library: /opt/ros/foxy/lib/liblistener_component.so
[INFO] [1665550184.808943962] [ComponentManager]: Found class: rclcpp_components::NodeFactoryTemplate<composition::Listener>
[INFO] [1665550184.809249919] [ComponentManager]: Instantiate class: rclcpp_components::NodeFactoryTemplate<composition::Listener>
[INFO] [1665550184.877423277] [talker]: Publishing: 'Hello World: 71'
[INFO] [1665550184.877769996] [listener]: I heard: [Hello World: 71]
[INFO] [1665550185.875934244] [talker]: Publishing: 'Hello World: 72'
[INFO] [1665550185.876612816] [listener]: I heard: [Hello World: 72]
[INFO] [1665550186.875510168] [talker]: Publishing: 'Hello World: 73'
[INFO] [1665550186.876478602] [listener]: I heard: [Hello World: 73]
[INFO] [1665550187.875740475] [talker]: Publishing: 'Hello World: 74'
[INFO] [1665550187.876527188] [listener]: I heard: [Hello World: 74]
[INFO] [1665550188.875847111] [talker]: Publishing: 'Hello World: 75'
[INFO] [1665550188.876574709] [listener]: I heard: [Hello World: 75]
....
```
#Creating a launch file
```bash
#Create a new directory to store launch files and write the launch file
---------------------------------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ mkdir launch
ulugbekmirzabakhromov@ubuntu:~$ cd launch
ulugbekmirzabakhromov@ubuntu:~/launch$ nano turtlesim_mimic_launch.py

#Run the launch file created above
----------------------------------
ulugbekmirzabakhromov@ubuntu:~/launch$ ros2 launch turtlesim_mimic_launch.py
[INFO] [launch]: All log files can be found below /home/ulugbekmirzabakhromov/.ros/log/2022-10-11-23-20-59-048056-ubuntu-74002
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [turtlesim_node-1]: process started with pid [74004]
[INFO] [turtlesim_node-2]: process started with pid [74006]
[INFO] [mimic-3]: process started with pid [74008]
[turtlesim_node-2] [INFO] [1665555660.604911859] [turtlesim2.sim]: Starting turtlesim with node name /turtlesim1/sim
[turtlesim_node-1] [INFO] [1665555660.609759335] [turtlesim1.sim]: Starting turtlesim with node name /turtlesim1/sim
[turtlesim_node-2] [INFO] [1665555660.642208649] [turtlesim2.sim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
[turtlesim_node-1] [INFO] [1665555660.645056958] [turtlesim1.sim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-10-12%20at%2015.28.55.png)

#To see the system in action, open a new terminal and run the commands below
```bash
ulugbekmirzabakhromov@ubuntu:~/launch$ ros2 topic pub -r 1 /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"
publisher: beginning loop
publishing #1: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=2.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=-1.8))

publishing #2: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=2.0, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=-1.8))
....
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/turtlesimlaunch.gif)

#Introspect the sytem with rqt_graph
```bash
ulugbekmirzabakhromov@ubuntu:~/launch$ rqt_graph
[INFO] [1665557607.422017603] [rclcpp]: signal_handler(signal_value=2)
```
![](https://github.com/ULUGBEK12194914/turtlesim_project/blob/main/screenshots/Screen%20Shot%202022-10-12%20at%2015.53.14.png)

#Integrating launch files into ROS 2 packages
```bash
#Create a workspace for the package to live in:
-----------------------------------------------
ulugbekmirzabakhromov@ubuntu:~$ mkdir -p launch_ws/src
ulugbekmirzabakhromov@ubuntu:~$ cd launch_ws/src
ulugbekmirzabakhromov@ubuntu:~/launch_ws/src$ ros2 pkg create py_launch_example --build-type ament_python
going to create a new package
package name: py_launch_example
destination directory: /home/ulugbekmirzabakhromov/launch_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['ulugbekmirzabakhromov <mirzabakhromov2001@gmail.com>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
...
#Writing the launch file
-------------------------
ulugbekmirzabakhromov@ubuntu:~/launch_ws/src$ cd py_launch_example/
ulugbekmirzabakhromov@ubuntu:~/launch_ws/src/py_launch_example$ ls
package.xml  py_launch_example  resource  setup.cfg  setup.py  test
ulugbekmirzabakhromov@ubuntu:~/launch_ws/src/py_launch_example$ nano my_script_launch.py

#Build and running the launch file
----------------------------------
ulugbekmirzabakhromov@ubuntu:~/launch_ws$ colcon build
Starting >>> py_launch_example
Finished <<< py_launch_example [1.22s]          

Summary: 1 package finished [1.43s]
ulugbekmirzabakhromov@ubuntu:~/launch_ws/src/py_launch_example$ ros2 launch my_script_launch.py
[INFO] [launch]: All log files can be found below /home/ulugbekmirzabakhromov/.ros/log/2022-10-18-02-37-36-481715-ubuntu-92643
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [92645]
[talker-1] [INFO] [1666085857.924744749] [talker]: Publishing: 'Hello World: 1'
[talker-1] [INFO] [1666085858.916853311] [talker]: Publishing: 'Hello World: 2'
[talker-1] [INFO] [1666085859.908849875] [talker]: Publishing: 'Hello World: 3'
[talker-1] [INFO] [1666085860.901022715] [talker]: Publishing: 'Hello World: 4'
[talker-1] [INFO] [1666085861.893365115] [talker]: Publishing: 'Hello World: 5'
[talker-1] [INFO] [1666085862.885724569] [talker]: Publishing: 'Hello World: 
....
```
