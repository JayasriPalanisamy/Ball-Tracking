# Task-2
1. The first file is an Image publisher node file, which will read  the video stream frame by frame,\
and publishes them through a specific topic.

2. The second file is an Image subscriber node file, which will subscribe to the image topic of tennis ball,\
extracts the image from ROS topic, converts it to an OpenCV image using cv_bridge, and applies the\
ball detection algorithm. 