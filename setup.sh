#!bin/bash

echo "--------- Updating package manager ---------"
sudo apt update
sudo apt upgrade

echo "--------- Installing openGL dependency ---------"
sudo apt install python-openGL -y

echo "--------- Setup complete ---------"