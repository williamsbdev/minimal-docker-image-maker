# A project for creating minimal Docker images

[![Build Status](https://travis-ci.org/williamsbdev/minimal-docker-image-maker.png)](https://travis-ci.org/williamsbdev/minimal-docker-image-maker)

The concept of this project is to find all the libraries for running an
application or process in a Docker container. This will lead to smaller Docker
images so that deploys are faster, disk usage is minimized, and attack surfaces
are decreased.

## Building a minimal Java Spring Boot application image with the OpenJDK installed on Centos 7

    docker build -t centos:java1.8.0_121 -f Dockerfile-java .

    rm -rf build-output

    docker run --rm -v "${PWD}:/data" -w /data centos:java1.8.0_121 python create_minimal_image.py /usr/lib/jvm/jre

    docker build -t minimal-java -f Dockerfile-minimal .

    docker build -t minimal-spring-boot -f Dockerfile-spring-boot .

or

    ./build-java.sh

Then to run Spring Boot application:

    docker run -p 8080:8080 minimal-spring-boot

## Building a minimal Ruby on Rails application image with the rvm and Ruby 2.3.3 installed on Centos 7

    docker build -t centos:ruby2.3.3 -f Dockerfile-ruby .

    rm -rf build-output

    docker run --rm -v "${PWD}:/data" -w /data centos:ruby2.3.3 python create_minimal_image.py

    docker build -t minimal-ruby -f Dockerfile-minimal .

    docker build -t minimal-rails -f Dockerfile-rails .

or

    ./build-ruby.sh

Then to run Spring Boot application:

    docker run -p 3000:3000 minimal-rails

# Running tests

    # create virtualenv if you'd like
    pip install -r requirements.txt
    py.test
