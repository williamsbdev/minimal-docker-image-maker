#!/bin/bash

# build build image
docker build -t centos:java1.8.0_121 .
# gather files for new minimal Java image
docker run -v "${PWD}:/data" -w /data centos:java1.8.0_121 python create_minimal_image.py /usr/lib/jvm
# build minimal Java image
docker build -t minimal-java -f Dockerfile-minimal-java .
# build minimal Java image with Spring Boot application
docker build -t minimal-spring-boot -f Dockerfile-spring-boot .
