#!/bin/bash

echo "****************************************"
echo " Setting up Capstone Environment"
echo "****************************************"

echo "Updating package manager..."
sudo add-apt-repository -y ppa:deadsnakes/ppa

echo "Installing Python 3.9 and Virtual Environment"
sudo apt-get update
sudo apt-get install -y python3.9 python3.9-venv

echo "Making Python 3.9 the default..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

echo "Checking the Python version..."
python3 --version

echo "Creating a Python virtual environment"
python3 -m venv venv

echo "****************************************"
echo " Capstone Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use:"
echo ""
echo "  source venv/bin/activate"
echo ""
echo "to activate the Python virtual envronment"
