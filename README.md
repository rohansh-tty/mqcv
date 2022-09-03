# mqcv
Template repo that helps in streaming video frames using OpenCV &amp; ZeroMQ


![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![ZeroMQ](https://img.shields.io/badge/ZeroMQ-DF0000.svg?style=for-the-badge&logo=ZeroMQ&logoColor=white)

## Usage

Run this command in terminal, before starting docker
```
$ xhost+
```

Build the docker container using docker file. Make sure camera device is on and not busy. 

To start the server

 ```
 $ python3 server.py
 ```
 
 To start the client

 ```
 $ python3 client.py
 ```
