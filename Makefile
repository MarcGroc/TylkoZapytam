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
	echo "Running tests for backend app"
	python backend/manage.py test app
	echo "Running tests for backend users"
	python backend/manage.py test users

migrations:
	echo "Making app migrations"
	python backend/manage.py makemigrations app
	echo "Making app migrate"
	python backend/manage.py migrate app
	echo "Making users migrations"
	python backend/manage.py makemigrations users
	echo "Making users migrate"
	python backend/manage.py migrate users

checkmigrations:
	python backend/manage.py makemigrations --check --no-input --dry-run

# Docker commands
build-backend:
	docker build . -f deployment/backend/Dockerfile -t backend

build-fronted:
	docker build . -f deployment/frontend/Dockerfile -t frontend

build-task-runner:
	docker build . -f deployment/task_runner/Dockerfile -t task-runner

docker-compose:
	docker-compose -f docker-compose.development.yml rm -s -v -f
	docker-compose -f docker-compose.development.yml up --build

