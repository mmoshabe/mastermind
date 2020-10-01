#! /bin/bash
wget https://zoom.us/client/latest/zoom_amd64.deb
apt install ./zoom_amd64.deb -y
apt install python3-pip -y
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install ./google-chrome-stable_current_amd64.deb -y
apt install virtualenv python3-virtualenv -y
systemctl unmask sleep.target suspend.target hibernate.target hybrid-sleep.target
pip3 install airtable-python-wrapper
sudo reboot     