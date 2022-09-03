FROM ubuntu:18.04

# install python3, pip, opencv & it's dependencies. 
RUN apt update && apt install -y python3-pip && pip3 install --upgrade pip
RUN apt install -y build-essential cmake unzip pkg-config libjpeg-dev libpng-dev libtiff-dev libsm6
RUN apt-get -y install libgl1-mesa-glx && python3 -m pip install opencv-python 

# install python3 packages from requirements.txt
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN python3 -m pip install -r requirements.txt

