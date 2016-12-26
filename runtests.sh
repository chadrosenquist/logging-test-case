#!/usr/bin/sh

export PYTHONPATH=$PWD
cd tests
python loggingtestcase_tests.py
if [ "$?" == "0" ]; then
    echo "Passed"
    exit 0
else
    echo "FAILED"
    exit 1
fi

