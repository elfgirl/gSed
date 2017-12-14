#!/bin/bash -e

WHEEL_DIR=/build

#pip wheel -vvv --wheel-dir=$WHEEL_DIR $@

cd $WHEEL_DIR/src
#python $WHEEL_DIR/src/setup.py --help bdist_wheel 

python $WHEEL_DIR/src/setup.py bdist_wheel -b $WHEEL_DIR/tmp/ --dist-dir $WHEEL_DIR/dest clean
rm -rf $WHEEL_DIR/src/*.egg-info
rm -rf $WHEEL_DIR/dest/lib
