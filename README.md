# A project for creating minimal Docker images

The concept of this project is to find all the libraries for running an
application or process in a Docker container. This will lead to smaller Docker
images so that deploys are faster, disk usage is minimized, and attack surfaces
are decreased.

## To get started

    docker build -t centos:java1.8.0_121 .

    docker run -v "${PWD}:/data" -w /data centos:java1.8.0_121 python create_minimal_image.py

# Running tests

    # create virtualenv if you'd like
    pip install -r requirements.txt
    pytest

# TODOS

[ ]: copy files found by command above into `build-output/` to be used by a subsequent Docker image
[ ]: test out that this actually works for a Java application
[ ]: create a script that does the build process so a single command needs to be run
