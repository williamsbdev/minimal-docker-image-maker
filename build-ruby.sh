#!/bin/bash

docker build -t centos:ruby2.3.3 -f Dockerfile-ruby .
rm -rf build-output
docker run --rm -v "${PWD}:/data" -w /data centos:ruby2.3.3 python create_minimal_image.py /usr/local/rvm/rubies/ruby-2.3.3
docker build -t minimal-ruby -f Dockerfile-minimal .
docker build -t minimal-rails -f Dockerfile-rails .
