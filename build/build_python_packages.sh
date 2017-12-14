#!/bin/bash -e

docker build -t python-compile packager
docker run --rm --volume "$(pwd)"/../modules/redware/:/build/src --volume "$(pwd)"/output:/build/dest/ python-compile
docker run --rm --volume "$(pwd)"/../modules/blueware/:/build/src --volume "$(pwd)"/output:/build/dest/ python-compile
docker run --rm --volume "$(pwd)"/../modules/core/:/build/src --volume "$(pwd)"/output:/build/dest/ python-compile
docker run --rm --volume "$(pwd)"/../modules/malware/:/build/src --volume "$(pwd)"/output:/build/dest/ python-compile

cp output/*redware*.whl "$(pwd)"/../docker-server/front-red/lib
cp output/*blueware*.whl "$(pwd)"/../docker-server/front-blue/lib
cp output/*core*.whl "$(pwd)"/../docker-server/front-core/lib
cp output/*iscm_malware*.whl "$(pwd)"/../docker-server/front-mal/lib

cp output/*.whl "$(pwd)"/../docker-server/worker-celery/lib
