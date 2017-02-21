# A project for creating minimal Docker images

The concept of this project is to find all the libraries for running an
application or process in a Docker container. This will lead to smaller Docker
images so that deploys are faster, disk usage is minimized, and attack surfaces
are decreased.

## Building a minimal Java Spring Boot application image with the OpenJDK installed on Centos 7

    docker build -t centos:java1.8.0_121 .

    docker run -v "${PWD}:/data" -w /data centos:java1.8.0_121 python create_minimal_image.py /usr/lib/jvm

    docker build -t minimal-java -f Dockerfile-minimal-java .

    docker build -t minimal-spring-boot -f Dockerfile-spring-boot .

or

    ./build.sh

Then to run Spring Boot application:

    docker run -p 8080:8080 minimal-spring-boot

# Running tests

    # create virtualenv if you'd like
    pip install -r requirements.txt
    pytest
