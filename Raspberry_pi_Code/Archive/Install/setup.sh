#!/bin/bash

sudo apt update && sudo apt upgrade

sudo apt install python3 python3-pip

curl -s 'https://raw.githubusercontent.com/zerotier/ZeroTierOne/master/doc/contact%40zerotier.com.gpg' | gpg --import && \
if z=$(curl -s 'https://install.zerotier.com/' | gpg); then echo "$z" | sudo bash; fi

sudo systemctl enable zerotier-one.service --now
sudo zerotier-cli join zerotierID
