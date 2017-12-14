#!/bin/bash -e

docker build -t python-compile packager
docker run --rm --volume "$(pwd)"/..:/build/src --volume "$(pwd)"/output:/build/dest/ python-compile
