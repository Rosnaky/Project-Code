#!/bin/bash

while true; do
        if ping -c 1 google.com &> /dev/null; then
		echo "Connected to Wi-Fi. Running Python script"
		echo "Activating venv"
		export DISPLAY=:0
		xhost +
		source /home/ronak/Desktop/project-code/venv/bin/activate
		python3 /home/ronak/Desktop/project-code/src/app.py
		break
	else
		echo "Not connected to Wi-Fi. Retrying in 5 seconds..."
		sleep 5
	fi
done


