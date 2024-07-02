# mqcv
Repo that helps in streaming video frames using OpenCV &amp; ZeroMQ


![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![ZeroMQ](https://img.shields.io/badge/ZeroMQ-DF0000.svg?style=for-the-badge&logo=ZeroMQ&logoColor=white)

## Introduction

This repository simply implements a video frame streaming system using OpenCV and ZeroMQ. The system allows real-time video frame transmission from a camera to a receiver, enabling efficient and reliable video streaming over a network.

## Why ZeroMQ and OpenCV Video Streaming?

ZeroMQ provides a lightweight and efficient way to establish a pub-sub messaging pattern, making it an ideal choice for real-time video streaming.
By using ZeroMQ, we can decouple the camera capture and video processing from the display and rendering, allowing for greater flexibility and scalability in our system. This is useful in applications where multiple cameras or displays are involved, or where the video processing requires significant computational resources.


## Prerequisites

* Camera device available and not in use
* Python 3.x installed on your system
* `xhost+` command executed in the terminal before starting the Docker container (allows the container to access the camera device)

## Usage

**Step 1:** Enable X11 Forwarding
Before starting the Docker container, you need to enable X11 forwarding on your system. Run the following command in your terminal:
```
$ xhost+
```

**Step 2:** Build the Docker Container
Build the Docker container using the provided Dockerfile:
```
$ docker build -t <image-name> .
```
Replace <image-name> with the desired name for your Docker image. Make sure the camera device is on and not busy during this step.

**Step 3:** Start the Server
To start the server, run the following command in your terminal:
```
$ python3 server.py
```
This command starts the server, which listens for incoming connections from the client.

**Step 4:** Start the Client
To start the client, run the following command in your terminal:
```
$ python3 client.py
```
This command starts the client, which connects to the server and captures video frames from the camera device.

## Notes

- Make sure the camera device is properly configured and connected to your system before running the application.
- The server and client scripts assume that the camera device is accessible and configured correctly.
- You may need to modify the Dockerfile or the server/client scripts to accommodate specific requirements for your camera device or system configuration.

## Troubleshooting

- If you encounter issues with X11 forwarding, try restarting the Docker container or checking the X11 display settings on your system.
- If you encounter issues with the camera device, try restarting the camera device or checking the camera settings on your system.
- If you encounter issues with the server or client scripts, try debugging the scripts or checking the error logs for more information.
