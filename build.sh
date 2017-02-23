#!/bin/bash

# build build image
docker build -t centos:java1.8.0_121 .
# remove build-output dir before gathering dependencies
rm -rf build-output
# gather files for new minimal Java image
docker run --rm -v "${PWD}:/data" -w /data centos:java1.8.0_121 python create_minimal_image.py /usr/lib/jvm
# build minimal Java image
docker build -t minimal-java -f Dockerfile-minimal .
# build minimal Java image with Spring Boot application
docker build -t minimal-spring-boot -f Dockerfile-spring-boot .
