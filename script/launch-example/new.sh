#! /bin/sh
if [ "$#" -eq 0 ]; then
    echo "$0"
    exit 0
fi
if [ "$#" -eq 1 ]; then
    echo "$0"
    echo "$1"
    exit 0
fi
if [ "$#" -eq 2 ]; then
    echo "$0"
    echo "$1"
    echo "$2"
    exit 0
fi