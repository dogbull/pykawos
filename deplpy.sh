#!/usr/bin/env bash

python setup.py bdist_wheel

last_file=$(ls -t dist | head -1)

twine upload dist/${last_file}
