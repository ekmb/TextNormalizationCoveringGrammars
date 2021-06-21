# /bin/bash

cd ../src && make -B
DIR=$PWD
echo $DIR
cd ../testing && python test.py
