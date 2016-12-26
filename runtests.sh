#!/usr/bin/sh

export PYTHONPATH=$PWD
python tests/runall.py
if [ "$?" == "0" ]; then
    echo "Passed"
    exit 0
else
    echo "FAILED"
    exit 1
fi

