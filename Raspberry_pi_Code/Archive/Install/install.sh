#!/bin/bash

sudo rfkill unblock wifi && echo

echo '
network={
	ssid="SSID"
	psk="PASSWD"
} ' | sudo tee -a /etc/wpa_supplicant/wpa_supplicant.conf >> /dev/null

sudo systemctl enable ssh.service --now
sudo reboot
