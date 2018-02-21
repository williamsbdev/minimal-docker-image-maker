# A project for creating minimal Docker images

[![Build Status](https://travis-ci.org/williamsbdev/minimal-docker-image-maker.png)](https://travis-ci.org/williamsbdev/minimal-docker-image-maker)

The concept of this project is to find all the libraries for running an
application or process in a Docker container. This will lead to smaller Docker
images so that deploys are faster, disk usage is minimized, and attack surfaces
are decreased. A version of Docker that supports multi stage Dockerfiles is
required.

# Targets
This Dockerfile supports multiple targets, specified with the `--target` optino to the `docker build` command. The following targets are supported:

1. `minimal-final`
   This is a minimal Java JRE container. It contains no apps or JARs to execute.

2. `spring-boot-example`
   This includes an example Spring Boot executable JAR and sets it to run by default

# Base operating system and JRE options
This Dockerfile supports multiple base operating systems and JREs. The base operating system
and JRE are specified via Docker build arguments. The following options are supported:

## Base operating system options
The following base operating systems may be selected from when supplying shared libraries
to the minimal docker container. Note: updates via the available package manager for each OS
are applied.

1. `ubuntu1604`
   This option selects Ubuntu 16.04 (from `ubuntu:16.04`)

2. `centos7`
   This option selects CentOS 7 (from `centos:7`)

## JRE options
The following JREs may be selected from when choosing the JRE to be included in the minimal
docker container.

1. `oracle-java-8u162`
   Note: Due to licensing issues, the file `server-jre-8u162-linux-x64.tar.gz` must be supplied in the build context when selecting this option.
   This file may be obtained from Oracle at http://www.oracle.com/technetwork/java/javase/downloads/server-jre8-downloads-2133154.html

2. `distro-openjdk-java-8`
   This selects the distribution's package for OpenJDK 8.
   * For `ubuntu`, this is `openjdk-8-jre-headless`
   * For `centos`, this is `java-1.8.0-openjdk-headless`

# Building a minimal image
The selected values for the base operating system and JRE are specified via `--build-arg` options to the `docker build` command.

## Example
This example uses Ubuntu 16.04 and the Oracle JRE:

    docker build --build-arg BASE=ubuntu1604 --build-arg JAVA=oracle-java-8u162 --target=minimal-final -t minimal-java -f Dockerfile .

## Building a minimal Java Spring Boot application image with the OpenJDK installed on Centos 7

    docker build --build-arg BASE=centos7 --build-arg JAVA=distro-openjdk-java-8 --target=spring-boot-example -t minimal-spring-boot -f Dockerfile .


Then to run Spring Boot application:

    docker run -p 8080:8080 minimal-spring-boot

# Running tests

    # create virtualenv if you'd like
    pip install -r requirements.txt
    py.test

# Known issues

1. All base OS images and JRE options are executed during `docker build` (or cached images are used). This can lead to lengthy build times.

2. Not all functionality has been tested. For example, NSS configuration is missing for libc to perform DNS lookups; it is unknown if sufficient support files have been included for distro-based OpenJDK packages (such as the ca-certificates-java package, etc.)
