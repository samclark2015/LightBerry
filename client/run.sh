#!/bin/sh
if [ -f "$1" ]; then
	source $1
fi

if [ ! -d "$DEVICE_CLASS" ] || [ ! -f "$DEVICE_CLASS/device.py" ]; then
	echo "Device class $DEVICE_CLASS not found! Exiting..."
	exit 1
fi

pip3 install -r requirements.txt -r $DEVICE_CLASS/requirements.txt

python3 /usr/src/app/main.py
