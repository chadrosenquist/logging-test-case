#!/usr/bin/sh

# Generate documentation for all the python files.
cd loggingtestcase
ls *.py | grep -v __init__ | cut -f 1 -d '.' | xargs -L 1 python -m pydoc -w
cd ..
mkdir -p doc
mv loggingtestcase/*.html doc
