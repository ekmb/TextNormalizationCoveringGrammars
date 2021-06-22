# /bin/bash

cd ../src && make -B
cd ../testing && python test.py
