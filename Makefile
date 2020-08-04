# Makefile for local development
setup: 
	@python3 -m venv venv
	chmod +x venv/bin/activate
	./venv/bin/activate
	@pip install -r requirements.txt

run:
	flask run
