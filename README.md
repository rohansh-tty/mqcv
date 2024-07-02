# mqcv
Repo that helps in streaming video frames using OpenCV &amp; ZeroMQ


![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![ZeroMQ](https://img.shields.io/badge/ZeroMQ-DF0000.svg?style=for-the-badge&logo=ZeroMQ&logoColor=white)


**Introduction**

This repository simply implements a video frame streaming system using OpenCV and ZeroMQ. The system allows real-time video frame transmission from a camera to a receiver, enabling efficient and reliable video streaming over a network.

**Why ZeroMQ and OpenCV Video Streaming?**

ZeroMQ provides a lightweight and efficient way to establish a pub-sub messaging pattern, making it an ideal choice for real-time video streaming.
By using ZeroMQ, we can decouple the camera capture and video processing from the display and rendering, allowing for greater flexibility and scalability in our system. This is useful in applications where multiple cameras or displays are involved, or where the video processing requires significant computational resources.


**Prerequisites**

* Camera device available and not in use
* `xhost+` command executed in the terminal before starting the Docker container (allows the container to access the camera device)

## Usage

Run this command in a terminal, before starting
```
$ xhost+
```

Make sure the camera device is on and not busy. 

To start the server

 ```
 $ python3 server.py
 ```
 
 To start the client

 ```
 $ python3 client.py
 ```

**Notes**

* Make sure to execute `xhost+` in the terminal before starting the Docker container to allow the container to access the camera device.
* Ensure that the camera device is available and not in use before starting the server.
* You can adjust the camera settings (e.g., resolution, frame rate) by modifying the `server.py` script.

**Troubleshooting**

* Verify that the camera device is available and not in use.



