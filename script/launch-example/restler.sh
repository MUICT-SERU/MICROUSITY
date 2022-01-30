#! /bin/sh

cd ../..
mkdir bin
python3 restler-fuzzer/build-restler.py --dest_dir ${PWD}/bin
