# /bin/bash

cd ../src && make -f Makefile_other -B
cd ../testing && python test.py
