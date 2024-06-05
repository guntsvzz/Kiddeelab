# Note: You can use any Debian/Ubuntu based image you want. 
FROM python:3.11.9-bookworm

# set work directory
WORKDIR /src/app

# https://vsupalov.com/docker-arg-env-variable-guide/
# https://bobcares.com/blog/debian_frontendnoninteractive-docker/
ARG DEBIAN_FRONTEND=noninteractive
# Timezone
ENV TZ="Asia/Bangkok"
RUN apt clean 
RUN apt update && apt upgrade -y
# Set timezone
RUN apt install -y tzdata
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# Set locales
# https://leimao.github.io/blog/Docker-Locale/
RUN apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LC_ALL en_US.UTF-8 
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
# COPY ./requirements.txt .

RUN apt update 
RUN apt install -y \
    iputils-ping \
    build-essential \
    sudo \
    python3-pip \
    python3-pygame 
    # -qqy x11-apps

#Basic
RUN pip install numpy
RUN pip install pandas
RUN pip install requests
RUN pip install tqdm
# RUN pip install --no-cache-dir uvicorn
# RUN pip install fastapi
RUN pip install ipykernel
RUN pip install streamlit
RUN pip install matplotlib
RUN pip install seaborn
RUN pip install scikit-learn
# RUN pip install yfinance
RUN pip install torch
RUN pip install torchvision
RUN pip install pygame
RUN pip install pgzero
RUN pip3 install opencv-python
# RUN pip install poetry 
# RUN pip install poethepoet

# ENV DISPLAY=host.docker.internal:0.0

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# clean apt cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# clean pip cache
RUN pip cache purge
# CMD tail -f /dev/null