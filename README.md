# A project for creating minimal Docker images

[![Build Status](https://travis-ci.org/williamsbdev/minimal-docker-image-maker.png)](https://travis-ci.org/williamsbdev/minimal-docker-image-maker)

The concept of this project is to find all the libraries for running an
application or process in a Docker container. This will lead to smaller Docker
images so that deploys are faster, disk usage is minimized, and attack surfaces
are decreased. A version of Docker that supports multi stage Dockerfiles is
required.

## Building a minimal Java Spring Boot application image with the OpenJDK installed on Centos 7

    docker build -t minimal-spring-boot -f Dockerfile-spring-boot .


Then to run Spring Boot application:

    docker run -p 8080:8080 minimal-spring-boot

# Running tests

    # create virtualenv if you'd like
    pip install -r requirements.txt
    py.test
