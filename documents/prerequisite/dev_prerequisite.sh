#!/bin/bash

echo "Setting Development machine ..."
echo "**** Installing packages for development machine, please wait ****"

echo "**** Installing Python Dev Package ****"
# This is to get Python.h and Python C API (embedding Python into C++)
apt-get --yes --force-yes install python3.5-dev
echo "**********************************"
