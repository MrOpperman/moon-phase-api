# Makefile for local development
setup: 
	@pip install -r requirements.txt

run:
	FLASK_ENV=development FLASK_APP=app.py flask run
