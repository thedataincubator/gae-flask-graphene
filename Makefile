SHELL=bash

.conda: requirements.txt
	pip install -r requirements.txt -t vendor && touch .conda

server:
	dev_appserver.py . --port=6100 --admin_port=6101 --api_port=6102
