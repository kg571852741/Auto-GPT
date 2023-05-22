#!/bin/bash

# Get the absolute path of the current directory
current_dir=$(pwd)

# Set the current directory as an external path
export PYTHONPATH=$PYTHONPATH:$current_dir

# return print
echo "The current directory has been set as an external path"