default: format

format:
	echo "Formatting app directory"
	black backend
	isort backend --profile black
	black deployment
	isort deployment --profile black
	echo "Formatted successfully"

lint:
	echo "Linting app directory"
	flake8 backend/
	echo "Linted successfully"

run-backend:
	echo "Running backend"
	python backend/manage.py runserver

run-frontend:
	echo "Running frontend"
	cd frontend && npm start

run-local:
	make -j run-backend run-frontend

tests:
	echo "Running tests for backend"
	python backend/manage.py test users

migrations:
	echo "Making migrations"
	python backend/manage.py makemigrations
	echo "Making migrate"
	python backend/manage.py migrate

checkmigrations:
	python backend/manage.py makemigrations --check --no-input --dry-run
# Docker commands
build-backend:
	docker build . -f backend/Dockerfile -t backend

build-fronted:
	docker build . -f frontend/Dockerfile -t frontend

build-task-runner:
	docker build . -f task_runner/Dockerfile -t task-runner


docker-compose:
	docker-compose -f docker-compose.development.yml rm -s -v -f
	docker-compose -f docker-compose.development.yml up --build

